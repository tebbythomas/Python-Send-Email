'''
Description:
Send email to a local email server.
This server can be set by running the Python command:
python3 -m smtpd -c DebuggingServer -n localhost:1025
'''
import smtplib
import os

FROM_EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
TO_EMAIL_ADDRESS = os.environ.get('EMAIL_USER2')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('localhost', 1025) as smtp:
    # To identify ourselves as an encrypted connection
    '''smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(FROM_EMAIL_ADDRESS, EMAIL_PASSWORD)'''

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this Saturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(FROM_EMAIL_ADDRESS, TO_EMAIL_ADDRESS, msg)
