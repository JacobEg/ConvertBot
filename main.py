# local imports
from constants import *
from conversion import *
from connect_to_discord import *

# stdlib imports
from sys import exit as sys_exit

# TODO: implement connecting to Discord server

def write_help():
    pass

def is_valid_unit(unit: str):
    pass

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

def main():
    if not discord:
        print("Connection failed. Exiting")
        sys_exit(1)
    

main()