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
TEMPERATURE_UNITS = {'celsius', 'c', 'fahrenheit', 'f', 'kelvin', 'k'}
LENGTH_UNITS = {'feet', 'foot', 'ft', 'meter', 'metres', 'meters', 'metres', 'm', 'yard', 'yd',
                'mile', 'miles', 'mi'}
MASS_UNITS = {'pound', 'pounds', 'lb', 'lbs', 'gram', 'g', 'ounce', 'ounces', 'oz'}
AREA_UNITS = {'sq_ft', 'sq_m', 'square_foot', 'square_feet', 'square_meter', 'square_metre',
              'square_meters', 'square_metres'}
VOLUME_UNITS = {'teaspoon', 'tsp', 'teaspoons', 'tablespoon', 'tbsp', 'tablespoons',
                'fluid_ounces', 'fluid_ounce', 'fl_oz', 'cup', 'cups', 'c', 'pints', 'pint', 'pt',
                'quart', 'quarts', 'qt', 'gallon', 'gallons', 'gal', 'liter', 'liters', 'litre',
                'litres', 'l'}
UNITS = TEMPERATURE_UNITS.union(LENGTH_UNITS).union(MASS_UNITS).union(AREA_UNITS).union(VOLUME_UNITS)

# metric prefixes, all in lowercase with their multiplier (* 10^value)
PREFIXES = {'exa': 18, 'peta': 15, 'tera': 12, 'giga': 9, 'mega': 6, 'kilo': 3, 'hecto': 2,
            'deka': 1, 'deci': -1, 'centi': -2, 'milli': -3, 'micro': -6, 'nano' : -9, 'pico': -12,
            'femto': -15, 'atto': -18}

BOT_HANDLE = "@convertbot"

HELP_MESSAGE = "Use: {} <num> <unit_to_convert> <result_unit>".format(BOT_HANDLE)
