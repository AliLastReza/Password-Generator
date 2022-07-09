import string

from random import choices


def generate_password(length=8, use_upper=False, use_lower=False, use_digit=False, use_symbol=False):
    pool = ''

    if use_upper:
        pool += string.ascii_uppercase

    if use_lower:
        pool += string.ascii_lowercase

    if use_digit:
        pool += string.digits

    if use_symbol:
        pool += string.punctuation

    if pool == '':
        pool = string.ascii_letters

    password = ''.join(choices(pool, k=length))
    return password


if __name__ == '__main__':
    print(generate_password(length=20, use_upper=True, use_lower=True, use_digit=True, use_symbol=True))
