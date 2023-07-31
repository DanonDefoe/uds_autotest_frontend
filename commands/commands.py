import random
import string


def generate_valid_email():
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, 6))
    email = 'E+', rand_string, '@setinbox.com'
    return email
