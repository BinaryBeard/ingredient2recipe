# Because main is always too cluttered...

import json
import requests
from colorama import Fore, Back, Style, init

# The secret sauce behind the personality of this program
def inform(msg):
    print('{}{}{}{}'.format(Style.BRIGHT, Back.BLACK, Fore.MAGENTA, msg))

# Just a simple abstraction of reading a file
def get_json_file(file_path):
    with open(file_path) as raw_data:
        json_data = json.load(raw_data)
        return json_data

# Just a simple abstraction of a restful GET
def get_json_url(url):
    request = requests.get(url)
    if request.status_code != 200:
        return { 'error': 'fatal', 'status_code': request.status_code, 'raw': request }
    else:
        return request.json()
