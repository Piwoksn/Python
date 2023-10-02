import smtplib

#Variables
sender = "piwoksn@gmail.com"
receiver = "mccoypiwoks@gmail.com"
password= "classicalnob95"
subject = "Testing Email with Python"
body= "Hello Friend it has been a while"

#mail Header
message = f"""
From: {sender}
To: {receiver}
Subject: {subject} \n
{body}

"""

#server Object to start or call server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    #login
    server.login(sender, password)
    print("Logged in")
    
    #send mail
    server.sendmail(sender, receiver, message)
    print("Email has been sent")
    
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")
    
except smtplib.SMTPConnectError:
    print('Connection Error')