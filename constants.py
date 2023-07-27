# stdlib imports
import re

INTEGER_REGEX = re.compile('\d+')
FLOAT_REGEX = re.compile('-?\d*\.\d+')

# different units, all in lowercase
# TODO: finish filling this out
UNITS = {'feet', 'foot', 'ft', 'pound', 'pounds', 'lb', 'lbs', 'meter', 'metres', 'meters',
         'metres', 'm', 'gram', 'grams', 'g'}

# metric prefixes, all in lowercase
PREFIXES = {'exa', 'peta', 'tera', 'giga', 'mega', 'kilo', 'hecto', 'deka', 'deci', 'centi',
            'milli', 'micro', 'nano', 'pico', 'femto', 'atto'}

