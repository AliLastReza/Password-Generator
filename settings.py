VERSION = '1.1.0'
DESCRIPTION = f"""Password Generator v{VERSION}
Generates a random password as you want."""

PROGRAM_NAME = 'password-generator'
EPILOG_MSG = """Wish you an awesome day.
Copyright 2022, Mohammad Ali Reza"""

DEFAULT_LENGTH = 8
LEVEL_CHOICES = ('weak', 'medium', 'strong')
LEVELS_SETTINGS = {
    'weak': {'length': 8,
             'use_lower': True,
             'use_digit': True, },
    'medium': {'length': 16,
               'use_upper': True,
               'use_lower': True,
               'use_digit': True, },
    'strong': {'length': 24,
               'use_upper': True,
               'use_lower': True,
               'use_digit': True,
               'use_symbol': True, },
}
