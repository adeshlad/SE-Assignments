from io import StringIO
from mailOTP import OtpService
import sys
import unittest
from unittest.mock import patch
from credentials import EMAIL, PASSWORD, OTP_LENGTH


class TestOTPService(unittest.TestCase):

    def setUp(self):
        self.otpService = OtpService(EMAIL, PASSWORD, OTP_LENGTH)
        self.otpService.startSmtpServer()

    def tearDown(self):
        pass

    def test_generateOtp(self):
        print("\n\t----------Testing For generateOTP----------\n")

        # First, generatedOtp is initialized Empty
        self.assertEqual(self.otpService.generatedOtp, "")

        # Generation OTP
        self.otpService.generateOtp()
        self.assertEqual(len(self.otpService.generatedOtp), 6)

    def test_sendMail(self):
        print("\n\t----------Testing For sendMail---------\n")

        expected_output = "OTP is sent to your Email Address.\n"

        with patch('sys.stdout', new = StringIO()) as output:
            self.otpService.generateOtp()
            self.otpService.sendOTP("test@test.com")
            self.assertEqual(output.getvalue(), expected_output)
    
    def test_validateOTP(self):
        print("\n\t----------Testing For validateOTP----------\n")

        with patch('sys.stdout', new = StringIO()) as output:
            self.otpService.generateOtp()
            self.otpService.validateOtp(self.otpService.generatedOtp)
            self.assertEqual(output.getvalue(), "OTP is correct.\n")

        with patch('sys.stdout', new = StringIO()) as output:
            self.otpService.generateOtp()
            self.otpService.validateOtp("")
            self.assertEqual(output.getvalue(), "OTP is incorrect.\n")

unittest.main()
