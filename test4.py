#make a bucle in python
import smtplib
from email.message import EmailMessage

# Set up the message
msg = EmailMessage()
msg['Subject'] = 'Test Email'
msg['From'] = 'dariodealmeidaasensio@gmail.com'
msg['To'] = 'dariodealmeidasensio@gmail.com'
msg.set_content('This is a test email message.')

# Connect to the SMTP server and send the message
with smtplib.SMTP('smtp.gmail.com', 535) as smtp:
    smtp.starttls()
    smtp.login('dariodealmeidaasensio@gmail.com', 'Gatito2009')
    smtp.send_message(msg)