from selenium.webdriver.common.by import By


class RegistrationPageLocators():
    NAME_FIELD = (By.CSS_SELECTOR, '#name')
    SURNAME_FIELD = (By.CSS_SELECTOR, '#surname')
    PHONE_FIELD = (By.CSS_SELECTOR, '#phone')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#email')
    COUNTRY_FIELD = (By.CSS_SELECTOR, '#s2id_residenceCountry')
    COUNTRY_RUSSIA = (By.CSS_SELECTOR, "#select2-drop")
    PASS1_FIELD = (By.CSS_SELECTOR, '#password')
    PASS2_FIELD = (By.CSS_SELECTOR, '#passwordConfirmation')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
