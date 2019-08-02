import argparse
from utility import get_json_file, get_json_url, inform, handle_error, join_ingredients, build_parser
from recipe import Recipe
from colorama import Fore, Back, Style, init

init(autoreset=True)

verbose_output = False

# Just a few helper functions

def debug(msg):
    if verbose_output:
        print('{}debug:{} {}'.format(Style.BRIGHT, Style.RESET_ALL, msg))

# Actual Start of main

# If we have a local configuration file, use it (just for the API Key)
config_key = get_json_file('./config.json')['api_key']

# Nice library to create some command line parsing
parser = build_parser(config_key)
args = parser.parse_args()
verbose_output = args.verbose

if config_key == args.key:
    debug('Using API Key from config.json')
else:
    debug('Not Using API Key from config.json')

cs_ingredients = join_ingredients(args.ingredients)
inform('\nHello!\n\nI am looking for a recipe with the following ingredients:\n  {}\n\n... hopefully I can find something yummy!\n'.format(cs_ingredients))

search_url = 'https://www.food2fork.com/api/search?key={}&q={}&sort=r'.format(args.key, cs_ingredients)
debug('GET {}'.format(search_url))

# If we're not in dev mode, make a call to the API
if args.dev == False:
    search_json = get_json_url(search_url)
else:
    search_json = get_json_file('./mocks/mock_get.json')

# Verify content and move on
if 'error' in search_json:
    handle_error(search_json['error'])
    debug(recipe_json)
elif search_json['count'] > 0:
    if search_json['count'] > 10:
        inform('I found a ton of recipes that you can create!\n')
    elif search_json['count'] > 1:
        inform('I found a few recipes that you can create!\n')
    else:
        inform('I found a single recipe that you can create!\n')

    inform('Generating the ingredient list now.\nI will highlight the ingredients you own...\n')
    rId = search_json['recipes'][0]['recipe_id']

    recipe_url = 'https://www.food2fork.com/api/get?key={}&rId={}'.format(args.key, rId)
    debug('GET {}'.format(recipe_url))

    # We made it this far, so we need to make another API call
    if args.dev == False:
        recipe_json = get_json_url(recipe_url)
    else:
        recipe_json = get_json_file('./mocks/mock_recipe.json')

    if 'error' in recipe_json:
        handle_error(recipe_json['error'])
        debug(recipe_json)
    else:
        # Populate the model and run the printing function
        new_recipe = Recipe(recipe_json)
        new_recipe.pretty_print_ingredients_diff(args.ingredients)
        inform('\nGood Luck Cooking!\n')
else:
    # Fail gracefully, we hope
    inform('Well...\n\nThere is nothing I can tell you to make with your list of ingredients...\n\nBye!')
