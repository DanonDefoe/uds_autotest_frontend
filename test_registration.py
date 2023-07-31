from constants.links import Links
from pages.pages import Pages


def test_new_company_registration(browser):
    page = Pages(browser, Links.TRIAL_COMPANY_REGISTRATION)
    page.open()

    page.fill_name()
    page.fill_surname()
    page.fill_phone()
    page.fill_email_and_password()
    page.select_country_russia()


