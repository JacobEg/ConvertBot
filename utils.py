'''
Implementing miscellaneous functions to be used throughout the program.
'''

from constants import PREFIXES, UNITS

def to_base_val(prefixed_val: float, prefix: str) -> float:
    '''
    Takes a metric value and converts it to its base value.
    E.g. prefixed_val = 1, prefix = 'kilo', result will be 1000 since there are 1000 meters in 1
    kilometer
    '''
    if not prefix:
        return prefixed_val
    #prefix = prefix.lower()
    if prefix not in PREFIXES:
        raise ValueError('"{}" is not a valid metric prefix'.format(prefix))
    return prefixed_val * 10**PREFIXES[prefix]

def to_prefixed_val(base_val: float, prefix: str) -> float:
    '''
    Takes a base metric value and converts it to its prefixed value.
    E.g. base_val = 1000, prefix = 'kilo', result will be 1 since there are 1000 meters in 1
    kilometer
    '''
    if not prefix:
        return base_val
    #prefix = prefix.lower()
    if prefix not in PREFIXES:
        raise ValueError('"{}" is not a valid metric prefix'.format(prefix))
    return base_val / 10**PREFIXES[prefix]

def is_valid_unit(unit: str) -> bool:
    '''
    Return True if unit is a valid unit accepted by the bot, False otherwise.
    '''
    base_unit = unit
    for prefix in PREFIXES.keys():
        if unit.startswith(prefix):
            base_unit = unit[len(prefix):]
            break
    return base_unit in UNITS

def parse_text(msg: str):
    '''
    @param - msg : str - the message in the Discord server
        should be of the format '@bothandle <num> <unit_to_convert> <result_unit>'
    @return tuple where index 0 is the original number, index 1 is the original unit,
        index 2 is the converted number, index 3 is the converted unit

    If badly formatted, write help message explaining how to use the bot and return None.
    If invalid number or unit(s), raise ValueError explaining the error.
    '''
    msg_list = msg.lower().split()
    if (len(msg_list) == 1 and msg_list[0] == BOT_HANDLE) or len(msg_list) < 4:
        write_help()
        return None
    units_to_print = None
    unit = msg_list[2]
    if is_valid_unit(unit):
        num = msg_list[1]
        if INTEGER_REGEX.match(num) or FLOAT_REGEX.match(num):
            num = float(num)
        else:
            raise ValueError("Bad number to convert")
        converted_unit = msg_list[3]
        if not is_valid_unit(converted_unit):
            raise ValueError("Bad result unit")
        converted_num = convert(num, unit, converted_unit)
        units_to_print = (num, unit, converted_num, converted_unit)
    else:
        raise ValueError("Bad unit to convert")
    return units_to_print

def convert(number: int | float, unit: str, converted_unit: str):
    pass