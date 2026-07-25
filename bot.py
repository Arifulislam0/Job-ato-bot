import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def post_to_blogger_via_email():
    # গিটহাব সিক্রেটস থেকে কনফিগারেশন রিড করা
    sender_email = os.environ.get('GMAIL_USER')
    sender_password = os.environ.get('GMAIL_APP_PASSWORD')
    blogger_mail = os.environ.get('BLOGGER_SECRET_EMAIL')
    
    # টেস্ট করার জন্য একটি সাধারণ ও নিখুঁত পোস্ট কন্টেন্ট
    job_title = "Ariful Tech-Job BD - Automated Post"
    job_content = """
    <h2>স্বাগতম Ariful Tech-Job BD তে!</h2>
    <p>এটি গিটহাব অ্যাকশন এবং পাইথন বট দিয়ে জিমেইলের মাধ্যমে স্বয়ংক্রিয়ভাবে প্রকাশিত একটি পোস্ট।</p>
    <p>সবকিছু এখন সফলভাবে কাজ করছে।</p>
    """
    
    # ইমেইল মেসেজ তৈরি
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = blogger_mail
    msg['Subject'] = job_title  # শুধু টাইটেল রাখলাম যাতে ব্লগার কোনো ঝামেলা না করে
    
    # এইচটিএমএল বডি যুক্ত করা
    msg.attach(MIMEText(job_content, 'html'))
    
    try:
        # জিমেইল এসএমটিপি সার্ভার কানেকশন
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, blogger_mail, msg.as_string())
        server.quit()
        print("১০০% সফল! ইমেইল ব্লগার সিক্রেট ঠিকানায় পাঠানো হয়েছে।")
    except Exception as e:
        print(f"ত্রুটি দেখা দিয়েছে: {e}")

if __name__ == "_main_":
    post_to_blogger_via_email()
