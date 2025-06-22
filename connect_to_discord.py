'''
For setting up the connection to the discord server.
'''

# stdlib imports
# import json

# PyPi module imports
import requests

# my imports
from constants import BOT_HANDLE, API_BASE_URL, API_VERSION

class DiscordBot:
    def __init__(self):
        pass

    def write_msg(self, msg: str):
        channel_id = 0 # TODO change this value!! Will need to get channel ID elsewhere
        url = '{}/v{}/channels/{}/messages'.format(API_BASE_URL, API_VERSION, channel_id)
        print('Writing "{}" to server using {}'.format(msg, url))

    def read_next_prompt(self) -> str:
        pass

discord = None