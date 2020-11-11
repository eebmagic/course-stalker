from main import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = config['email']
target = config['target']
password = config['password']

number = config['number']

sms_gateway = config['sms_gateway']
smtp = "smtp.gmail.com" 
port = 587

def send_sms(body):
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


def send_email(body=None):
    subject = "Subject: Automated Message\n"
    if body == None:
        body = "Default notification text."
    msg = f'{subject}{body}'

    #email send request
    try:
        # Setup email account
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(email, password)

        # Send email
        msg = MIMEText(msg, "plain")
        server.sendmail(email, target, msg.as_string())
        server.close()

        print ('EMAIL SENT!')
    except Exception as e:
        print(e)
        print ('Something went wrong...')
