from colorama import Fore, Back, Style, init

# Abstraction at its best!
def has_ingredient(line, ingredient):
    return line.find(ingredient) >= 0

# Just a simple method to inject some ANSI escape codes for UI
def highlight_ingredient(line, ingredient):
    start_pos = line.find(ingredient)
    end_pos = start_pos + len(ingredient) + len(Style.BRIGHT)
    start_bold = line[:start_pos] + Style.BRIGHT + line[start_pos:]
    final_bold = start_bold[:end_pos] + Style.NORMAL + start_bold[end_pos:]
    return final_bold

class Recipe(object):
    def __init__(self, dict):
        # Essentially building a model on the stuff we care about
        rec = dict['recipe']
        self.title = rec['title']
        self.id = rec['recipe_id']
        # A few of the recipes have nasty white spaces... Gone
        self.ingredients = list(map(lambda s: s.strip(), rec['ingredients']))
        self.social_rank = rec['social_rank']
        self.f2f_url = rec['f2f_url']

    # Method that could be used later
    def pretty_print(self):
        print('{}{}'.format(Fore.CYAN, self.title))
        print('{}Ingredients:'.format(Fore.YELLOW))
        for i in range(len(self.ingredients)):
            print('  {}* {}'.format(Fore.MAGENTA, self.ingredients[i]))

    # Get a nice diff of on-hand vs need-to-obtain ingredients
    def pretty_print_ingredients_diff(self, ingredients):
        print('{}{}'.format(Fore.CYAN, self.title))
        print('{}Ingredients:'.format(Fore.YELLOW))
        for i in range(len(self.ingredients)):
            recipe_ing = self.ingredients[i]
            ing_str = ''
            for j in range(len(ingredients)):
                search_ing = ingredients[j]
                if has_ingredient(recipe_ing, search_ing):
                    ing_str = highlight_ingredient(recipe_ing, search_ing)
            if len(ing_str) == 0:
                # Looks like we don't have the ingredient on hand
                print('  {}* {}'.format(Fore.RED, recipe_ing))
            else:
                print('  {}* {}'.format(Fore.GREEN, ing_str))
