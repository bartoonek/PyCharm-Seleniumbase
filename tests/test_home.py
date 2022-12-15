from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):            #methods have to begin with word TEST
        #open homepage
        self.open('https://practice.automationbro.com/')

        #assert page tittle
        self.assert_title('Practice E-Commerce Site – Automation Bro')

        #assert logo
        self.assert_element('.custom-logo-link')

        #click on the get started button and assert the url
        self.click('#get-started')
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, 'https://practice.automationbro.com/#get-started')
        self.assert_true("get-started" in get_started_url)    #if "get-started" is in URL: true, if not false

        #get the text of header and assert the value
        self.assert_text('Think different. Make different.', 'h1')

        #scroll to bottom and assert the copyright text
        self.scroll_to_bottom()
        self.assert_text('Copyright © 2020 Automation Bro', '.tg-site-footer-section-1')

    def test_menu_links(self):     #pytest -k "test_menu_links" -s jeżeli chcemy uruchomic tylko 1 test

        expected_links = ['Home', 'About', 'Shop', 'Blog', 'Contact', 'My account']

        #open url
        self.open("https://practice.automationbro.com/")

        #find menu links elements
        menu_links_el = self.find_elements("//*[starts-with(@id, 'menu-item')]")

        #loop through our menu links
        for idx, links_el in enumerate(menu_links_el):
            print(idx, links_el.text)

