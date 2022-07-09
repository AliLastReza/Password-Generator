import argparse
import string

from random import choices

from settings import *


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
    parser = argparse.ArgumentParser(prog=PROGRAM_NAME,
                                     epilog=EPILOG_MSG,
                                     fromfile_prefix_chars='@',
                                     description=DESCRIPTION,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-len', '--length', type=int, default=DEFAULT_LENGTH, help="Length of password")
    parser.add_argument('-up', '--upper', help="Use upper case characters", action='store_true')
    parser.add_argument('-lw', '--lower', help="Use lower case characters", action='store_true')
    parser.add_argument('-d', '--digit', help="Use digits", action='store_true')
    parser.add_argument('-s', '--symbol', help="Use symbols", action='store_true')

    args = parser.parse_args()

    print(generate_password(length=args.length, use_upper=args.upper, use_lower=args.lower, use_digit=args.digit,
                            use_symbol=args.symbol))
