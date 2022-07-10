import argparse

from settings import *


def create_argparser():
    parser = argparse.ArgumentParser(epilog=EPILOG_MSG,
                                     fromfile_prefix_chars='@',
                                     description=DESCRIPTION,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-l', '--level', type=str, choices=LEVEL_CHOICES)
    parser.add_argument('-len', '--length', type=int, default=DEFAULT_LENGTH, help="Length of password")
    parser.add_argument('-up', '--upper', action='store_true', help="Use upper case characters")
    parser.add_argument('-lw', '--lower', action='store_true', help="Use lower case characters")
    parser.add_argument('-d', '--digit', action='store_true', help="Use digits")
    parser.add_argument('-s', '--symbol', action='store_true', help="Use symbols")

    return parser
