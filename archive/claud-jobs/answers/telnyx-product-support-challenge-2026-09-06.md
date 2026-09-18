# Telnyx - Product Support Engineer EMEA (Remote) - take-home challenge answers
Written 2026-09-06 from the pcap in the Sep 4 email (thread 1a06aaa57812900f). Submit link: https://app3.greenhouse.io/tests/6a680a27148d8a7dbdeae48b5112c030
READ THIS BEFORE ANY TELNYX INTERVIEW. Facts below come straight from the capture (4 packets, TCP 5060, Nov 19 2020).

## Task 1. Viewing the SIP flow sequence in Wireshark
1. Open the pcap in Wireshark (File > Open). Type `sip` in the display filter bar to show only SIP messages; `sip || sdp` also shows the media offer.
2. Telephony > VoIP Calls: select the call and click Flow Sequence. This draws the ladder diagram with the two endpoints as columns and each SIP message (INVITE, 100 Trying, 403, ACK) as an arrow with its timestamp.
3. Telephony > SIP Flows gives the same ladder directly. Statistics > Flow Graph (limit to displayed packets, flow type TCP or all) is the generic version.
4. Expand a packet in the middle pane (Session Initiation Protocol > Message Header) to read Request-URI, From, To, Via, Call-ID, the Reason header and the SDP body.
Note: this call runs SIP over TCP (transport=TCP, port 5060), so Wireshark reassembles the TCP segments; if the ladder looks empty, enable "Allow subdissector to reassemble TCP streams" under the TCP protocol preferences.

## Task 2. Which IP is the customer, which is Telnyx, and how I know
- Customer: 69.215.131.228 (public) using ephemeral source port 36744. The device behind it has private address 192.168.1.69 (the Via and Contact headers carry 192.168.1.69:58834, so the softphone sits behind NAT). It is the side that sends the INVITE and the ACK, its User-Agent is "Z 3.3.25608 r25552" (Zoiper), and the SDP says c=IN IP4 69.215.131.228.
- Telnyx: 192.76.120.10 on port 5060. It receives the INVITE and replies with "100 Telnyx trying" and the 403. The Server header says "kamailio (5.3.6)", which is the Telnyx SIP proxy, the Request-URI is sip.telnyx.com, and sip.telnyx.com lists 192.76.120.10 as the US region signaling IP address 1 (the Europe signaling addresses are 185.246.41.140/141, so this customer is registered against the US SIP region).

## Task 3. Number dialed and attempted caller ID
- Dialed number: 7085952391, from the INVITE Request-URI `sip:7085952391@sip.telnyx.com` and the To header. It is a 10-digit US number dialed without the +1 country code.
- Caller ID attempted: `zach`. The From header is `<sip:zach@sip.telnyx.com>`, and the P-Asserted-Identity header is absent, so Zoiper is presenting the SIP connection username as the caller ID instead of a phone number. Telnyx rejects it: `SIP/2.0 403 Caller Origination Number is Invalid D35` with `Reason: Q.850;cause=21;text="CALL_REJECTED"`.

## Task 4. Email to the customer

Subject: Your Zoiper calls failing with 403 - caller ID fix

Hi,

Thanks for sending the capture, it made this quick to pin down. Good news: your Zoiper setup is registering and reaching Telnyx correctly. The call is being rejected by our platform on purpose because of the caller ID it presents.

What the capture shows
- Your softphone (Zoiper, public IP 69.215.131.228) sends an INVITE to 7085952391 over TCP to our SIP proxy at 192.76.120.10.
- We answer "100 Trying" and then "403 Caller Origination Number is Invalid" (Q.850 cause 21, call rejected).
- The From header in your INVITE is sip:zach@sip.telnyx.com. In other words the call is trying to use your SIP username "zach" as the outbound caller ID. Outbound calls must present a valid phone number that you own on Telnyx, so the call is rejected before it ever leaves our network.

How to fix it (about two minutes)
1. In the Mission Control Portal go to Numbers and copy one of your Telnyx numbers in E.164 format, for example +13125550123. If you do not have a number yet, buy one under Numbers > Search & Buy, then assign it to your SIP connection.
2. Set it as the caller ID on the connection: Voice > SIP Connections > your connection > Outbound tab > "Caller ID override" (or the Outbound Voice Profile default caller ID). Save.
3. Set the same number in Zoiper so it stops sending "zach": Settings > Accounts > your Telnyx account > Advanced, and put the number in the Caller ID field (some Zoiper versions expose this as "Display name" or "Auth username / Username" split; the Username stays your SIP username, the Caller ID becomes the number). Restart the account.
4. Dial in full international format, +17085952391, rather than the bare 10 digits. Telnyx accepts both for US destinations, but E.164 removes any ambiguity, especially once you call other countries.

Then place a test call to your cell. You should see it ring within a couple of seconds. If you still get a 403, send me the Call-ID from Zoiper's log or a fresh pcap and I will check the connection settings on our side.

Two things to double check while you are in the portal: the SIP connection has an Outbound Voice Profile attached (Voice > Outbound Voice Profiles), and the profile allows the destination (US) with enough credit. Both are common causes of the next error people hit after fixing caller ID.

Let me know how the test goes.

Best regards,
Prabhavit Gupta
Telnyx Support
