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
# TODO: consider whether or not we should accept abbreviations; will make computation
# significantly more challenging
TEMPERATURE_UNITS = {'celsius', 'c', 'fahrenheit', 'f', 'kelvin', 'k'}
LENGTH_UNITS = {'feet', 'foot', 'ft', 'meter', 'metres', 'meters', 'metres', 'm', 'yard', 'yd',
                'mile', 'miles', 'mi', 'inch', 'inches', 'in'}
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

# conversion amounts
FEET_PER_METER = 3.28084
FEET_PER_YARD = 3.0
FEET_PER_MILE = 5280.0
YARDS_PER_MILE = 1760.0
INCHES_PER_FOOT = 12.0
FAHRENHEIT_AT_0_CELSIUS = 32.0
KELVIN_AT_0_CELSIUS = 273.15
FAHRENHEIT_PER_CELSIUS = 1.8
OUNCES_PER_POUND = 16.0
GRAMS_PER_OUNCE = 28.3495
GRAMS_PER_POUND = 453.592
QUARTS_PER_GALLON = 4
PINTS_PER_GALLON = QUARTS_PER_GALLON * 2
CUPS_PER_GALLON = PINTS_PER_GALLON * 2
FL_OZ_PER_GALLON = CUPS_PER_GALLON * 10
TBSP_PER_GALLON = CUPS_PER_GALLON * 16
TSP_PER_GALLON = CUPS_PER_GALLON * 48