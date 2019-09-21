# Python code to send out an email to multiple recipients with both images pdfs as attachments

<p>
<b>Description:</b>
<br />
<b>mail_demo.py</b>: is a Python script to send an email to multiple recipients, with multiple attachments
(images and pdfs) and also send out the <b>message body as an HTML</b> instead of just
plain text
<br />
In this program both the sender and recipients have gmail addresses but any email can be used
<br />
The from and to email addresses have been read from the environment variables in the interest of privacy.
<br />
Also for this to work with gmail, you'll need to create an app password using this link: https://myaccount.google.com/apppasswords
<br />
<br />
<b>Libraries and modules used:</b>
<br />
smtplib, os, imghdr, email.message
<br />
<br />
<b>mail_demo_server.py</b>: is a Python code to send an email on a locally setup demo server on the terminal
