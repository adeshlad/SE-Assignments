import smtplib
import re
from random import randint
from credentials import EMAIL, PASSWORD, OTP_LENGTH


# function to get email address
def getEmail():
    print("Enter email address to receive OTP. ", end="")
    email = input().strip()

    if checkValidEmail(email):
        return email
    else:
        print("Please enter valid email address. ")
        getEmail()


# function to validate receiver email address
def checkValidEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email) != None:
        return True
    else:
        return False


# function to generate OTP of desired length
def generateOtp(length):
    lowerBound = int("1" + "0"*(length-1))
    upperBound = int("9"*length)
    otp = str(randint(lowerBound, upperBound))

    return otp


# function to start SMTP server
def startSmtpServer(email, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)

    return server

# function to send otp to receiver
def sendOTP(server, message, receiver):
    server.sendmail(EMAIL, receiver, message)
    server.quit()
    print("OTP is sent to your Email Address.")

# function for validate entered OTP
def validateOtp(generatedOtp):
    print("Enter OTP. ")
    otp = input().strip()

    if generatedOtp == otp:
        print("OTP is correct.")
    else:
        print("OTP is incorrect.")
        validateOtp(generatedOtp)

def main():
    receiver = getEmail()
    server = startSmtpServer(EMAIL, PASSWORD)
    generatedOtp = generateOtp(OTP_LENGTH)
    message = "Your One Time Password is " + generatedOtp
    sendOTP(server, message, receiver)
    validateOtp(generatedOtp)

main()
