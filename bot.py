import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def post_to_blogger_via_email():
    sender_email = os.environ.get("GMAIL_USER")
    sender_password = os.environ.get("GMAIL_APP_PASSWORD")
    blogger_mail = os.environ.get("BLOGGER_SECRET_EMAIL")

    job_title = "Private Job Circular 2026 - GitHub Automation"
    job_content = """
    <p>এটি গিটহাব অ্যাকশনস (GitHub Actions) থেকে অটোমেটিক পোস্ট করা হয়েছে।</p>
    <br>
    <p><b>পদের নাম:</b> প্রাইভেট ব্যাংক অফিসার</p>
    <p><b>আবেদনের শেষ তারিখ:</b> ৩০ জুলাই ২০২৬</p>
    <br>
    <a href="https://arifultechjobbd.blogspot.com/" target="_blank">বিস্তারিত দেখুন ও আবেদন করুন</a>
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = blogger_mail
    msg['Subject'] = job_title

    msg.attach(MIMEText(job_content, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, blogger_mail, msg.as_string())
        server.quit()
        print("GitHub Actions এর মাধ্যমে ব্লগে সফলভাবে পোস্ট হয়েছে!")
    except Exception as e:
        print(f"পোস্ট করতে সমস্যা হয়েছে: {e}")

if _name_ == "_main_":
    post_to_blogger_via_email()
