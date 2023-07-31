from constants.links import Links
from pages.base_page import RegistrationPage


class Pages(RegistrationPage):
    def go_to_registration_page(self):
        login_link = self.browser.find_element(*Links.TRIAL_COMPANY_REGISTRATION)
        login_link.click()
