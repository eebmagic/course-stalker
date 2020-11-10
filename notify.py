import smtplib
from main import config
from email.mime.text import MIMEText

# Load email and password
email = config['email']
target = config['target']
password = config['password']


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
        print(f"sending email with {msg.as_string() = }")
        server.sendmail(email, target, msg.as_string())
        server.close()

        # print ('Email sent!')
    except Exception as e:
        print(e)
        print ('Something went wrong...')
