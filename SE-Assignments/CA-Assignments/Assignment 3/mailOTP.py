import smtplib
import re
from random import randint
from credentials import EMAIL, PASSWORD, OTP_LENGTH

class OtpService:
    def __init__(self, email, password, length):
        self.email = email
        self.password = password
        self.length = length
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.generatedOtp = ""

    # function to generate OTP of desired length
    def generateOtp(self):
        lowerBound = int("1" + "0"*(self.length-1))
        upperBound = int("9"*self.length)
        self.generatedOtp = str(randint(lowerBound, upperBound))

    # function to start SMTP server
    def startSmtpServer(self):
        self.server.starttls()
        self.server.login(self.email, self.password)


    # function to send otp to receiver
    def sendOTP(self, receiver):
        message = "Your OTP is " + self.generatedOtp
        self.server.sendmail(self.email, receiver, message)
        self.server.quit()
        print("OTP is sent to your Email Address.")

    # function for validate entered OTP
    def validateOtp(self, otp):
        if self.generatedOtp == otp:
            print("OTP is correct.")
            return True
        else:
            print("OTP is incorrect.")
            return False


sender = OtpService(EMAIL, PASSWORD, OTP_LENGTH)

print("Enter receiver email address. ", end="")
receiverEmail = input()
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
while not re.fullmatch(regex, receiverEmail):
    print("Enter valid email address.")
    receiverEmail = input()


sender.generateOtp()
sender.startSmtpServer()
sender.sendOTP(receiverEmail)

print("Enter OTP. ")
otp = input().strip()
while not sender.validateOtp(otp):
    print("Enter OTP. ")
    otp = input().strip()

