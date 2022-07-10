import string
from random import choices

from argparser import create_argparser
from settings import LEVELS_SETTINGS


def main():
    parser = create_argparser()

    args = parser.parse_args()

    if args.level is not None:
        level_settings = LEVELS_SETTINGS[args.level]
        print(generate_password(**level_settings))
    else:
        print(generate_password(length=args.length, use_upper=args.upper, use_lower=args.lower, use_digit=args.digit,
                                use_symbol=args.symbol))


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
        pool = string.ascii_lowercase + string.digits

    password = ''.join(choices(pool, k=length))
    return password


if __name__ == '__main__':
    main()
