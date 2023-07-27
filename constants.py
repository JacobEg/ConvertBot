'''
For initializing the constants that will be used in the implementation of the bot. Hopefully,
everything should be able to be funneled into UNITS for use in the parse_text function in main.py.
'''

# stdlib imports
import re

# regex
INTEGER_REGEX = re.compile('\d+')
FLOAT_REGEX = re.compile('-?\d*\.\d+')

# different units, all in lowercase
# TODO: finish filling this out
UNITS = {'feet', 'foot', 'ft', 'pound', 'pounds', 'lb', 'lbs', 'meter', 'metres', 'meters',
         'metres', 'm', 'gram', 'grams', 'g'}

# metric prefixes, all in lowercase
PREFIXES = {'exa', 'peta', 'tera', 'giga', 'mega', 'kilo', 'hecto', 'deka', 'deci', 'centi',
            'milli', 'micro', 'nano', 'pico', 'femto', 'atto'}

BOT_HANDLE = "@convertbot"
