from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from commands.commands import generate_valid_email
from constants.links import RegistrationFormData
from constants.locators import RegistrationPageLocators


class RegistrationPage():
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def fill_name(self):
        name_field = self.browser.find_element(*RegistrationPageLocators.NAME_FIELD)
        name_field.send_keys(RegistrationFormData.NAME)

    def fill_surname(self):
        surname_field = self.browser.find_element(*RegistrationPageLocators.SURNAME_FIELD)
        surname_field.send_keys(RegistrationFormData.SURNAME)

    def fill_phone(self):
        phone_field = self.browser.find_element(*RegistrationPageLocators.PHONE_FIELD)
        phone_field.send_keys(RegistrationFormData.PHONE)

    def fill_email_and_password(self):
        email = generate_valid_email()
        email_field = self.browser.find_element(*RegistrationPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*RegistrationPageLocators.PASS1_FIELD)
        password_field.send_keys(str(email) + 'm')

        confirmation_field = self.browser.find_element(*RegistrationPageLocators.PASS2_FIELD)
        confirmation_field.send_keys(str(email) + 'm')

    def select_country_russia(self):
        select_russia = Select(self.browser.find_element(*RegistrationPageLocators.COUNTRY_RUSSIA))
        select_russia.select_by_visible_text('Российская Федерация')

        # country_field = self.browser.find_element(*RegistrationPageLocators.COUNTRY_FIELD)
        # country_field.click()
        # time.sleep(1)
        # select_russia = self.browser.find_element(*RegistrationPageLocators.COUNTRY_RUSSIA)
        # select_russia.click()


def is_element_present(self, how, what):
    try:
        self.browser.find_element(how, what)
    except NoSuchElementException:
        return False
    return True
