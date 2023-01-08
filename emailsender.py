from email.message import EmailMessage

import ssl
import smtplib

reciever=input(str('enter email address of reciever....'))
email_receiver = reciever

subject = input(str('enter the subject...'))
body = input(str('enter the body of the email....'))
email_sender = 'ognasion@gmail.com'
email_password  = 'hpskpcofzqumnvct'
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())