# local imports
from constants import *
from conversion import *

# TODO: implement connecting to Discord server

def parse_text(msg: str):
    '''
    @param - msg : str - the message in the Discord server
    @return list of tuples where index 0 is the original number, index 1 is the original unit,
    index 2 is the converted number, index 
    '''
    units_to_print = []
    msg_list = msg.lower().split()
    for i in range(1, len(msg_list)):
        unit = msg_list[i]
        if unit in UNITS:
            num = msg_list[i-1]
            if INTEGER_REGEX.match(num) or FLOAT_REGEX.match(num):
                num = float(num)
            else:
                continue
            converted_num, converted_unit = convert(num, unit)
            units_to_print.append((num, unit, converted_num, converted_unit))
    return units_to_print


def convert(number: int | float, unit: str):
    pass