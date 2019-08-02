import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src import recipe, utility

def test_recipe_title():
    recipe_json = utility.get_json_file('./mocks/mock_recipe.json')
    new_recipe = recipe.Recipe(recipe_json)
    assert new_recipe.title == 'Vietnamese Style Spicy Caramel Chicken Wings'

def test_recipe_id():
    recipe_json = utility.get_json_file('./mocks/mock_recipe.json')
    new_recipe = recipe.Recipe(recipe_json)
    assert new_recipe.id == '4500'

def test_recipe_ingredients():
    recipe_json = utility.get_json_file('./mocks/mock_recipe.json')
    new_recipe = recipe.Recipe(recipe_json)
    assert len(new_recipe.ingredients) == 7

def test_recipe_social_rank():
    recipe_json = utility.get_json_file('./mocks/mock_recipe.json')
    new_recipe = recipe.Recipe(recipe_json)
    assert new_recipe.social_rank == 99.99999999999856

def test_recipe_f2f_url():
    recipe_json = utility.get_json_file('./mocks/mock_recipe.json')
    new_recipe = recipe.Recipe(recipe_json)
    assert new_recipe.f2f_url == 'http://food2fork.com/view/4500'

def test_pretty_print(capsys):
    recipe_json = utility.get_json_file('./mocks/mock_recipe.json')
    new_recipe = recipe.Recipe(recipe_json)
    new_recipe.pretty_print()
    captured = capsys.readouterr()
    assert captured.out == '\x1b[36mVietnamese Style Spicy Caramel Chicken Wings\n\x1b[33mIngredients:\n  \x1b[35m* 1/4 cup water\n  \x1b[35m* 1/2 cup sugar\n  \x1b[35m* 1/4 cup fish sauce\n  \x1b[35m* 2 tablespoons lime juice (~1 lime)\n  \x1b[35m* 2 tablespoons chili sauce (such as sriracha) or to taste\n  \x1b[35m* 2 cloves garlic, chopped\n  \x1b[35m* 2 pounds chicken wings, rinsed and pat dry\n'

def test_pretty_print_ingredients_diff(capsys):
    recipe_json = utility.get_json_file('./mocks/mock_recipe.json')
    new_recipe = recipe.Recipe(recipe_json)
    new_recipe.pretty_print_ingredients_diff(['chicken'])
    captured = capsys.readouterr()
    assert captured.out == '\x1b[36mVietnamese Style Spicy Caramel Chicken Wings\n\x1b[33mIngredients:\n  \x1b[31m* 1/4 cup water\n  \x1b[31m* 1/2 cup sugar\n  \x1b[31m* 1/4 cup fish sauce\n  \x1b[31m* 2 tablespoons lime juice (~1 lime)\n  \x1b[31m* 2 tablespoons chili sauce (such as sriracha) or to taste\n  \x1b[31m* 2 cloves garlic, chopped\n  \x1b[32m* 2 pounds \x1b[1mchicken\x1b[22m wings, rinsed and pat dry\n'
