from seleniumbase import BaseCase



class ContactPage(BaseCase):
    ## Contact Page Locators
    contact_us_link = "[data-target='#exampleModal']"
    contact_email_css = "#recipient-email"
    contact_name_css = "#recipient-name"
    contact_textarea_css = "#message-text"
    send_button_css = "[onclick='send()']"
    close_button = "#exampleModal .btn-secondary"
    url = "https://www.demoblaze.com/"
    email = "itsforme60@gmail.com"
    password = "ymlilgee1991"
    texts = "Standalone Test Automation IDE and Built-in Integration with Visual Studio. Ensure quality across web and desktop, with reusability of elements across projects. Industry-Leading Support. Flexible Pricing. 30-day Free Trial. Automated Record/Playback."


    def load_page(self):
        self.open(self.url)
        if self.assert_element(self.contact_us_link):
            self.click(self.contact_us_link)
            self.type(self.contact_email_css,self.email)
            self.type(self.password,self.password)
            self.type(self.contact_textarea_css,)
            self.click(self.send_button_css, self.texts)
        else:
            raise Exception("Element not found")
    def verify_contact_page_element(self):
        self.assert_elements(self.contact_us_link,self.contact_email_css,self.contact_textarea_css,self.contact_name_css,self.send_button_css,self.close_button)
