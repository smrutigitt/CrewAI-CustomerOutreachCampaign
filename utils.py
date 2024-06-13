import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(subject, from_email, to_email, body):
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    smtp_server = os.getenv("SMTP_SERVER", "smtp.example.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    email_password = os.getenv("EMAIL_PASSWORD")

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, email_password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise e

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")

def pretty_print_result(result):
    from IPython.display import Markdown
    return Markdown(result)
