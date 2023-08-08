'''
Implementing miscellaneous functions to be used throughout the program.
'''

from constants import PREFIXES, UNITS, BOT_HANDLE, INTEGER_REGEX, FLOAT_REGEX

def to_base_val(prefixed_val: float, prefix: str) -> float:
    '''
    Takes a metric value and converts it to its base value.
    E.g. prefixed_val = 1, prefix = 'kilo', result will be 1000 since there are 1000 meters in 1
    kilometer
    @param prefixed_val: float - base metric value to be converted to its prefixed val
    @param prefix: str - the prefix of the input val
    @return float - the prefixed val
    '''
    if not prefix:
        return prefixed_val
    #prefix = prefix.lower()
    if prefix not in PREFIXES:
        raise ValueError('"{}" is not a valid metric prefix'.format(prefix))
    return prefixed_val * (10**PREFIXES[prefix])

def to_prefixed_val(base_val: float, prefix: str) -> float:
    '''
    Takes a base metric value and converts it to its prefixed value.
    E.g. base_val = 1000, prefix = 'kilo', result will be 1 since there are 1000 meters in 1
    kilometer
    @param base_val: float - base metric value to be converted to its prefixed val
    @param prefix: str - prefix to adjust base_val to
    @return float - the prefixed val
    '''
    if not prefix:
        return base_val
    #prefix = prefix.lower()
    if prefix not in PREFIXES:
        raise ValueError('"{}" is not a valid metric prefix'.format(prefix))
    return base_val / (10**PREFIXES[prefix])

def is_valid_unit(unit: str) -> bool:
    '''
    Return True if unit is a valid unit accepted by the bot, False otherwise.
    @param unit : str - unit to check if valid
    @return bool - true if the unit is valid, else false
    '''
    base_unit = unit
    for prefix in PREFIXES.keys():
        if unit.startswith(prefix):
            base_unit = unit[len(prefix):]
            break
    return base_unit in UNITS

def parse_text(msg: str):
    '''
    @param msg : str - the message in the Discord server
        should be of the format '@bothandle <num> <unit_to_convert> <result_unit>'
    @return tuple - index 0 is the original number, index 1 is the original unit,
        index 2 is the converted number, index 3 is the converted unit

    If badly formatted, return None.
    If invalid number or unit(s), raise ValueError explaining the error.
    '''
    msg_list = msg.lower().split()
    if (len(msg_list) == 1 and msg_list[0] == BOT_HANDLE) or len(msg_list) < 4:
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

def convert(source_val: float, source_unit: str, converted_unit: str) -> float:
    '''
    Takes a source val and unit and converts it to the equivalent value in the converted unit
    @param source_val: float - value of source unit
    @param source_unit: str - unit of source unit ('mile', 'celsius', etc)
    @param converted_units: str - unit of converted unit ('kilometer', 'fahrenheit', etc)
    @return float -  value of converted unit
    '''
    pass