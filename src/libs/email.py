import smtplib
import ssl
from email_config import *


context = ssl.create_default_context()


try:
    server = smtplib.SMTP(SMTP_SERVER, EMAIL_PORT)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    
except Exception as e:
    print(e)
finally:
    server.quit()
