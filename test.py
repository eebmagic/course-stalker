import notifier
import notify
from config import config
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

email = config['email']
sms_gate = config['sms_gateway']
number = config['number']

# recipient = f'{number}{sms_gate}'

body = "This is a test of message sending"

# print(recipient)

# msg = MIMEMultipart()
# msg['From'] = email
# msg['To'] = recipient


notify.send_email(body)