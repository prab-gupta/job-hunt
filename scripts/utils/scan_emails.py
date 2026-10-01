import imaplib
import email
from email.header import decode_header
import datetime
import json
import csv

# Credentials
USERNAME = "prabhavitg@gmail.com"
PASSWORD = "xeoa zwqw caqg uqza"

def get_recent_emails():
    try:
        # Connect to Gmail
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(USERNAME, PASSWORD)
        mail.select("inbox")

        # Calculate date for the last 25 days
        date_since = (datetime.date.today() - datetime.timedelta(days=25)).strftime("%d-%b-%Y")
        
        # Search for all emails since that date
        status, messages = mail.search(None, f'(SINCE "{date_since}")')
        
        if status != "OK":
            print("Failed to search emails.")
            return []

        email_ids = messages[0].split()
        
        results = []
        # Get the last 150 emails to be safe
        for e_id in email_ids[-150:]:
            res, msg_data = mail.fetch(e_id, '(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT FROM DATE)])')
            if res != "OK": continue
            
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    
                    subject = decode_header(msg.get("Subject", ""))[0][0]
                    if isinstance(subject, bytes):
                        try:
                            subject = subject.decode()
                        except:
                            subject = str(subject)
                    
                    from_ = msg.get("From", "")
                    date_ = msg.get("Date", "")
                    
                    # Basic filtering for job-related keywords or domains
                    subject_lower = str(subject).lower()
                    from_lower = str(from_).lower()
                    
                    job_keywords = ["application", "interview", "update", "status", "next steps", "unfortunately", "regret", "offer", "resume", "cv", "candidate"]
                    ats_domains = ["greenhouse.io", "lever.co", "myworkday.com", "ashbyhq.com", "smartrecruiters.com", "bamboohr.com", "workable.com", "personio", "recruitee"]
                    
                    is_job_related = any(kw in subject_lower for kw in job_keywords) or any(ats in from_lower for ats in ats_domains)
                    
                    if is_job_related:
                        results.append({
                            "date": date_,
                            "from": from_,
                            "subject": subject
                        })
        
        mail.logout()
        return results
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    emails = get_recent_emails()
    with open("job_emails.json", "w") as f:
        json.dump(emails, f, indent=2)
    print(f"Found {len(emails)} job-related emails.")
