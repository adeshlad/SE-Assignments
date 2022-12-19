import smtplib
import re
from random import randint

def checkValidEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def sendOTP():
    email = input("Enter Email. ")

    if checkValidEmail(email):
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("adeshslad2@gmail.com", "pdfhdwmwwdirmrhq")
        
        # generating OTP
        otp = str(randint(100_000, 999_999))
        s.sendmail("adeshslad2@gmail.com", email, "The One Time Password (OTP) is " + otp)
        
        # terminating the session
        s.quit()
    
    else:
        print("Invalid Email!")
        sendOTP()

sendOTP()
