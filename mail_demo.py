'''
Description:
Python script to send an email to multiple recipients, with multiple attachments
(images and pdfs) and also send out the message body as an HTML instead of just
plain text
'''
import smtplib
import os
import imghdr
from email.message import EmailMessage

FROM_EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = [os.environ.get('EMAIL_USER2'), os.environ.get('EMAIL_USER3')]

files = ['/Users/tebbythomas/Desktop/Company_Profits.png', '/Users/tebbythomas/Desktop/Late_Bloomers.png', '/Users/tebbythomas/Desktop/Tebby_Thomas_Resume.pdf']

msg = EmailMessage()
msg['Subject'] = 'Automated HTML email sent via Python to multiple recipients with attachments'
msg['From'] = FROM_EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg_body = 'Please check if you have received {}attachments'.format(len(files))
# The email body displays this text only if it cannot display the HTML content
# add in the enxt line
msg.set_content(msg_body)
# The email is received with this HTML data as the email body
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        # Determines what the file type of the image is
        if 'jpg' in f.name or 'png' in f.name:
            file_type = imghdr.what(f.name)
        file_name = f.name
        file_name = file_name.split('/')
        filename = file_name[-1]
    if 'jpg' in filename or 'png' in filename:
        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=filename)
    else:
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(FROM_EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("Email has been sent")
