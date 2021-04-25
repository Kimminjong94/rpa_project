import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls() #모든 내용이 암호화되어 젆오
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "test mail"
    body = "mail body"

    msg = f"Subject: {subject}\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, "easyletgothen@gmail.com", msg)