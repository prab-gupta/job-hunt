# Telnyx Customer Issue — SIP Call Failure Analysis

**Capture:** `CustomerIssue.pcap` (4 packets, SIP over TCP, 2020-11-19 20:32:39 UTC)
**Prepared by:** Prabhavit
**Date:** 2026-09-06

## Summary

| Question | Answer |
|---|---|
| What failed | Telnyx rejected the call at the SIP (Session Initiation Protocol, the call-signaling layer) proxy: `SIP/2.0 403 Caller Origination Number is Invalid D35` |
| Why | The softphone is sending the SIP username `zach` as the caller ID (From header). Telnyx requires a phone number the customer owns on their account, in +E.164 format (international format: `+`, country code, number, e.g. `+17085952391`). |
| Customer IP | `69.215.131.228` (public, behind NAT, i.e. a home/office router doing Network Address Translation). Softphone LAN address `192.168.1.69`. |
| Telnyx IP | `192.76.120.10` (`sip.telnyx.com`, US signaling IP, TCP 5060) |
| Dialed number | `7085952391` (10-digit US national format, acceptable, not the cause) |
| Caller ID attempted | `zach` |
| Fix | Set **Caller ID Override** on the SIP connection's Outbound tab to the customer's Telnyx number in +E.164 (mode Always). Confirm a number is assigned to the connection and an Outbound Voice Profile is attached. |

---

## Task 1 — How to view the SIP flow sequence in Wireshark

### Steps

1. **Install Wireshark.** Download from https://www.wireshark.org/download.html (current stable 4.6.x; macOS `.dmg`, Windows `.exe`). On macOS, also install the bundled ChmodBPF helper when prompted (only needed for live capture, not for opening a file).
2. **Open the capture.** File → Open → `CustomerIssue.pcap` (or drag the file onto Wireshark).
3. **Filter to SIP.** Type `sip` in the display-filter bar and press Enter. Four packets remain: INVITE, 100 Trying, 403, ACK.
4. **Open the flow sequence.** Telephony → **SIP Flows** → select the row for this call (Call-ID `YmJiZjQ1ZTcwYWQ2NDJlMTQ3Mzg5NmM0Yjc1OTQzOTc.`) → click **Flow Sequence**. Wireshark draws a ladder diagram: each host is a vertical line, each SIP message is an arrow labelled with the method or status line and timestamps.
   - Alternative: Telephony → **VoIP Calls** → select the call → **Flow Sequence**. Both open the same window. SIP Flows is the more reliable entry point for a *failed* INVITE like this one, because VoIP Calls only lists detected calls.
   - Alternative: Statistics → **Flow Graph** → tick "Limit to display filter" → Flow type "All Flows". Same ladder, also shows ports.
5. **Read the raw messages.** Click any packet, expand **Session Initiation Protocol** in the Packet Details pane to see every header. Because this is SIP over **TCP**, you can also right-click the INVITE → Follow → **TCP Stream** to read the whole conversation as text (client-to-server in red, server-to-client in blue).
6. **Useful filters** while investigating:
   - `sip.Method == "INVITE"` — only requests that start calls
   - `sip.Status-Code == 403` or `sip.Status-Code >= 400` — only failures
   - `sip.Call-ID == "YmJiZjQ1ZTcwYWQ2NDJlMTQ3Mzg5NmM0Yjc1OTQzOTc."` — one dialog
   - `sip.From contains "zach"` — all messages from this account

### Flow sequence for this capture

Customer = `69.215.131.228`, Telnyx = `192.76.120.10`.

| # | Time (UTC) | Direction | SIP message | Meaning |
|---|---|---|---|---|
| 1 | 20:32:39.703 | Customer → Telnyx | `INVITE sip:7085952391@sip.telnyx.com`, `From: <sip:zach@sip.telnyx.com>` | Call attempt. Caller ID sent as "zach". |
| 2 | 20:32:39.708 | Telnyx → Customer | `100 Telnyx trying` | Telnyx received the request. |
| 3 | 20:32:39.805 | Telnyx → Customer | `403 Caller Origination Number is Invalid D35`, `Reason: Q.850;cause=21;text="CALL_REJECTED"` | Call rejected: caller ID is not a valid number. |
| 4 | 20:32:39.833 | Customer → Telnyx | `ACK` | Softphone acknowledges the rejection. Call over in 130 ms. |

### Command-line equivalents

tshark (Wireshark's CLI, ships with Wireshark):

```bash
tshark -r CustomerIssue.pcap -Y sip -T fields -e frame.time_relative -e ip.src -e ip.dst -e sip.Request-Line -e sip.Status-Line
```

```bash
tshark -r CustomerIssue.pcap -q -z sip,stat
```

```bash
tshark -r CustomerIssue.pcap -q -z flow,any,network,sip
```

Notes: `-z voip,calls` does not exist in tshark, and `-z follow,sip` is documented as not implemented (use `-z follow,tcp,ascii,0`). tshark was not installed on the machine used for this analysis; the commands above were checked against the tshark man page.

Without Wireshark at all, macOS/Linux `tcpdump` prints the SIP text directly. This is what was used to verify every header quoted in this document:

```bash
tcpdump -A -nn -tttt -r CustomerIssue.pcap
```

---

## Task 2 — Which IP is the customer's and which is Telnyx's

| Role | Address | Port |
|---|---|---|
| Customer, public side (after NAT) | `69.215.131.228` | TCP 36744 (ephemeral) |
| Customer, softphone on the LAN | `192.168.1.69` | 58834 |
| Telnyx SIP proxy | `192.76.120.10` | TCP 5060 |

### How I know

1. **Direction of the messages.** The INVITE and the ACK are sent *by* `69.215.131.228` *to* `192.76.120.10`. The 100 Trying and the 403 come back the other way. On an outbound call the customer's device is always the one sending the INVITE, so `69.215.131.228` is the customer and `192.76.120.10` is the provider.

2. **Telnyx's published IP list.** https://sip.telnyx.com/ lists the US signaling addresses for `sip.telnyx.com` as `192.76.120.10` and `64.16.250.10`, with UDP 5060, TCP 5060 and TLS 5061 as supported transports. The Request-URI in the INVITE is `sip.telnyx.com`, so the destination IP is simply what that hostname resolved to. `192.76.120.10:5060` over TCP matches exactly.

3. **Identity headers.** The INVITE carries `User-Agent: Z 3.3.25608 r25552`. The `Z` prefix is the Zoiper softphone (the customer said they use Zoiper). The responses carry a `Server:` header and the reason phrase `100 Telnyx trying`, which only the Telnyx side would produce.

4. **NAT evidence.** The customer's `Via` header says `192.168.1.69`, an RFC 1918 private address that cannot be routed on the Internet. Yet the packet arrived at Telnyx with source `69.215.131.228`. That means a home/office router rewrote the address (NAT). Telnyx confirms this in its replies by adding `received=69.215.131.228;rport=36744` to the Via (RFC 3261 §18.2.1 and RFC 3581): the server writes back the address and port it *actually* saw. Zoiper's `Contact` header and the SDP `c=IN IP4 69.215.131.228` line also use the public address, which is Zoiper's own NAT handling doing its job.

5. **Port numbers.** 5060 is the standard SIP port and is where a provider listens. 36744 is a random high (ephemeral) port, typical of a client opening a connection.

6. **Bonus: authentication is not the problem.** The INVITE has `CSeq: 2` and a `Proxy-Authorization` header. That means the first INVITE (CSeq 1, not in this capture) was challenged with a 407 and this is the retry with credentials. Telnyx answered 403 rather than another 407, so the username and password were accepted. The rejection is a policy decision, not a login failure.

---

## Task 3 — What number is dialed and what is being used as caller ID

**Dialed number: `7085952391`**
- Found in the Request-URI: `INVITE sip:7085952391@sip.telnyx.com;transport=TCP` and in the `To:` header.
- This is 10-digit US national format (708 is a Chicago-area code). It is not in +E.164 form (`+17085952391`), but Telnyx accepts national format for outbound calls when the connection's Localization Country is United States, which is the default validation rule (https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats). The dialed number is **not** why the call failed.

**Caller ID being attempted: `zach`**
- Found in the `From:` header: `From: <sip:zach@sip.telnyx.com;transport=TCP>;tag=7ec95301`.
- Telnyx determines caller ID from the *user part* of these headers, in priority order: P-Preferred-Identity, P-Asserted-Identity, Remote-Party-Id, From (https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy). The INVITE has none of the first three, so Telnyx falls back to From, and the user part of From is `zach`.
- `zach` is the SIP connection username (it also appears in `Contact:` and in `Proxy-Authorization: username="zach"`). Zoiper places the account username in the From user part by default; nothing in the customer's setup told it to send a phone number instead.

**Why Telnyx rejected it.** Telnyx's SIP response-code reference defines this exact message: "D35 — Caller Origination Number is Invalid. The Caller ID in your SIP INVITE is not valid... please make sure your FROM/PAID/RPID headers contain +E.164 number formats." (https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes). The caller ID must also be a number that exists on the customer's Telnyx account (or has been added as a Verified Number). `zach` fails number validation outright (D35 is the format/validity check; a well-formed number belonging to another Telnyx customer would return D36, and an unverified non-Telnyx number D51), so the proxy returned 403 D35 with `Reason: Q.850;cause=21` (ISDN "call rejected", a generic policy rejection). Telnyx's troubleshooting guide calls this the most common cause of failed calls on new credential-based connections: "The caller ID will often either be blank or, if you are using a credential-based SIP connection, your SIP username" (https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion).

---

## Task 4 — Response email to the customer

**Subject:** Re: 403 error on outbound calls from Zoiper - caller ID fix

Hi Zach,

Thanks for the pcap, it made this quick to diagnose. Your setup is very close to working.

**What is happening**

Your call reaches Telnyx and your login is accepted. We then reject it with:

    SIP/2.0 403 Caller Origination Number is Invalid D35

That means the caller ID on the call is not a valid phone number. Zoiper is sending your SIP username, "zach", as the caller ID. Telnyx requires a phone number you own on your account, in E.164 format (+1 followed by the ten digits for a US number).

The number you dialed, 708-595-2391, is fine and is not the cause. I do recommend dialing it as +17085952391 going forward.

**How to fix it**

1. In Mission Control, confirm you have a Telnyx phone number and that it is assigned to this SIP connection (Numbers → My Numbers).
2. Go to Voice → SIP Trunking, click the pencil icon on your connection, open the **Outbound** tab. In **Caller ID Override**, enter your Telnyx number as +1XXXXXXXXXX, set the mode to **Always**, set **Localization Country** to United States, and Save.
3. On the same tab, confirm an **Outbound Voice Profile** is attached and your account balance is positive. Either missing also causes a 403.
4. Place a test call to +17085952391.

**Side note:** your softphone reports Zoiper 3.x over TCP, while the guide you followed is for Zoiper 5 Pro over TLS. Neither caused this failure, but I recommend TLS (port 5061) once calls are working, so your signaling is encrypted.

If the test call still fails, reply with a fresh capture and the time of the call, and we will check the logs on our side.

References: [Troubleshooting call completion](https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion), [Caller ID policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy), [SIP connection outbound settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings)

Best regards,
Prabhavit
Telnyx Support

---

## Appendix A — Raw SIP messages (from `tcpdump -A`)

```
INVITE sip:7085952391@sip.telnyx.com;transport=TCP SIP/2.0
Via: SIP/2.0/TCP 192.168.1.69:58834;branch=z9hG4bK-d8754z-6f8830100a40fac2-1---d8754z-
Max-Forwards: 70
Contact: <sip:zach@69.215.131.228:58834;transport=TCP>
To: <sip:7085952391@sip.telnyx.com;transport=TCP>
From: <sip:zach@sip.telnyx.com;transport=TCP>;tag=7ec95301
Call-ID: YmJiZjQ1ZTcwYWQ2NDJlMTQ3Mzg5NmM0Yjc1OTQzOTc.
CSeq: 2 INVITE
Allow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE
Content-Type: application/sdp
Proxy-Authorization: Digest username="zach",realm="sip.telnyx.com",nonce="a5000778-d70a-4a52-a5e0-5dae6f6fe1b8",uri="sip:7085952391@sip.telnyx.com;transport=TCP",response="183cff39436bf519d82ac4e05a98e232",cnonce="f8582ed6bb0747f1a28195cbed864927",nc=00000001,qop=auth,algorithm=MD5,opaque="27211c50-4875-4397-9467-4eacf0355c50/10.15.196.4"
Supported: replaces, norefersub, extended-refer, timer, X-cisco-serviceuri
User-Agent: Z 3.3.25608 r25552
Allow-Events: presence, kpml
Content-Length: 243

v=0
o=Z 0 0 IN IP4 69.215.131.228
s=Z
c=IN IP4 69.215.131.228
t=0 0
m=audio 8004 RTP/AVP 3 110 8 0 98 101
a=rtpmap:110 speex/8000
a=rtpmap:98 iLBC/8000
a=fmtp:98 mode=20
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=sendrecv
```

```
SIP/2.0 100 Telnyx trying
Via: SIP/2.0/TCP 192.168.1.69:58834;branch=z9hG4bK-d8754z-6f8830100a40fac2-1---d8754z-;rport=36744;received=69.215.131.228
To: <sip:7085952391@sip.telnyx.com;transport=TCP>
From: <sip:zach@sip.telnyx.com;transport=TCP>;tag=7ec95301
Call-ID: YmJiZjQ1ZTcwYWQ2NDJlMTQ3Mzg5NmM0Yjc1OTQzOTc.
CSeq: 2 INVITE
Server: kamailio (5.3.6 (x86_64/linux))
Content-Length: 0
```

```
SIP/2.0 403 Caller Origination Number is Invalid D35
Via: SIP/2.0/TCP 192.168.1.69:58834;rport=36744;received=69.215.131.228;branch=z9hG4bK-d8754z-6f8830100a40fac2-1---d8754z-
Max-Forwards: 69
From: <sip:zach@sip.telnyx.com;transport=TCP>;tag=7ec95301
To: <sip:7085952391@sip.telnyx.com;transport=TCP>;tag=941StD4Fyr8tD
Call-ID: YmJiZjQ1ZTcwYWQ2NDJlMTQ3Mzg5NmM0Yjc1OTQzOTc.
CSeq: 2 INVITE
Accept: application/sdp
Allow: INVITE, ACK, BYE, CANCEL, OPTIONS, MESSAGE, INFO, UPDATE, REFER, NOTIFY
Supported: path
Allow-Events: talk, hold, conference, refer
Reason: Q.850;cause=21;text="CALL_REJECTED"
Content-Length: 0
```

```
ACK sip:7085952391@sip.telnyx.com;transport=TCP SIP/2.0
Via: SIP/2.0/TCP 192.168.1.69:58834;branch=z9hG4bK-d8754z-6f8830100a40fac2-1---d8754z-
Max-Forwards: 70
To: <sip:7085952391@sip.telnyx.com;transport=TCP>;tag=941StD4Fyr8tD
From: <sip:zach@sip.telnyx.com;transport=TCP>;tag=7ec95301
Call-ID: YmJiZjQ1ZTcwYWQ2NDJlMTQ3Mzg5NmM0Yjc1OTQzOTc.
CSeq: 2 ACK
Content-Length: 0
```

## Appendix B — Sources

Telnyx
- SIP signaling and media IPs: https://sip.telnyx.com/
- Telnyx SIP response codes (D35 definition): https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
- Troubleshooting call completion (403 causes, Caller ID Override): https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- Caller ID policy, header precedence: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy
- Caller ID number policy: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- SIP connection number formats / Localization: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
- SIP connection inbound and outbound settings: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
- Caller ID Override steps: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- Zoiper 5 Pro setup guide (the one the customer followed): https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup
- Verified Numbers: https://developers.telnyx.com/docs/voice/verified-numbers
- Zoiper 3 setup guides (Mac / Linux): https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac , https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux

Wireshark
- Download: https://www.wireshark.org/download.html
- SIP Flows window: https://www.wireshark.org/docs/wsug_html_chunked/ChTelSIPFlows.html
- VoIP Calls window / Flow Sequence: https://www.wireshark.org/docs/wsug_html_chunked/ChTelVoipCalls.html
- Flow Graph: https://www.wireshark.org/docs/wsug_html_chunked/ChStatFlowGraph.html
- Follow TCP Stream: https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html
- SIP display filter fields: https://www.wireshark.org/docs/dfref/s/sip.html
- tshark man page: https://www.wireshark.org/docs/man-pages/tshark.html

Standards
- RFC 3261 (SIP), §18.2.1 `received` parameter, §21.4.4 403 Forbidden: https://www.rfc-editor.org/rfc/rfc3261.html
- RFC 3581 (`rport`, symmetric response routing): https://www.rfc-editor.org/rfc/rfc3581.html
- RFC 3326 (Reason header carrying Q.850 cause): https://www.rfc-editor.org/rfc/rfc3326.html
- RFC 1918 (private address space): https://www.rfc-editor.org/rfc/rfc1918.html
