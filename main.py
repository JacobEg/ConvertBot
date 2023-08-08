'''
Main file for program.
'''
# local imports
from constants import *
from conversion import *
from connect_to_discord import discord
from utils import *

# stdlib imports
from sys import exit as sys_exit
from sys import stderr

def main():
    if not discord:
        print("Connection failed. Exiting", file=stderr)
        sys_exit(1)

main()