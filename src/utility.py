# Because main is always too cluttered...

import json
import requests
import argparse
from colorama import Fore, Back, Style, init

# The secret sauce behind the personality of this program
def inform(msg):
    print('{}{}{}{}'.format(Style.BRIGHT, Back.BLACK, Fore.MAGENTA, msg))

# Just a simple abstraction of reading a file
def get_json_file(file_path):
    try:
        with open(file_path) as raw_data:
            json_data = json.load(raw_data)
            return json_data
    except:
        return {}

# Just a simple abstraction of a restful GET
def get_json_url(url):
    request = requests.get(url)
    if request.status_code != 200:
        return { 'error': 'fatal', 'status_code': request.status_code, 'raw': request }
    else:
        return request.json()

# Pretty generic error handling
def handle_error(err_msg):
    if err_msg == 'limit':
        inform('Well, dangit!\n\nIt looks like your API Key has reached its limit for the day...\n\nYou should probably fix that!')
    else:
        inform('I ran into some kind of fatal error...')

# This will need to be a bit more verbose in the future... so it's abstracted now
def join_ingredients(ing_list):
    return ','.join(ing_list)

# Just building the parser out of main so we can test
def build_parser(config_key):
    parser = argparse.ArgumentParser(description='Find a great recipe', prog='src/main.py')
    parser.add_argument('ingredients', metavar='INGREDIENT', nargs='+', help='Space delimited list of ingredients')
    parser.add_argument('-k', '--key', metavar='KEY', help='API key for food2fork', default=config_key)
    parser.add_argument('-d', '--dev', help='run in developer mode', action='store_true')
    parser.add_argument('-v', '--verbose', help='run in verbose mode', action='store_true')
    return parser
