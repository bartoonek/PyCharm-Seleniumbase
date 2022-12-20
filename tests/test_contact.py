from seleniumbase import BaseCase

#pytest -k "xxxxx"

class ContactPage(BaseCase):

    def test_input(self):
        # open page
        self.open('https://practice.automationbro.com/contact/')

        # fill the fills
        self.send_keys(".contact-name input", "Test_name")
        self.send_keys(".contact-email input", "mail@test.com")
        self.send_keys(".contact-phone input", "123456789")
        self.send_keys(".contact-message textarea", "Test message")

        # click submit button

        self.click("#evf-submit-277")

        # veryfi submit message

        self.assert_text("Thanks for contacting us! We will be in touch with you shortly", "div[role=alert]")
