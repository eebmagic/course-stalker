# from config import config
from main import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = config['email']
password = config['password']

sms_gateway = config['sms_gateway']
smtp = "smtp.gmail.com" 
port = 587

def send_sms(number, body):
    recipient = f'{number}{sms_gateway}'
    body = f'\n{body}'

    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, password)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient

    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    server.sendmail(email, recipient, body.encode('utf8'))

    server.quit()
