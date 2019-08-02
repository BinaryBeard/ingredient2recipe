# Ingredient2Recipe

So you have a bunch of ingredients and don't know what to make? Sweet. Just fire me up and watch the magic happen! 


## Usage

```
usage: main.py [-h] [-k KEY] [-d] [-v] INGREDIENT [INGREDIENT ...]

Find a great recipe

positional arguments:
  INGREDIENT         Space delimited list of ingredients

optional arguments:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  API key for food2fork
  -d, --dev          run in developer mode
  -v, --verbose      run in verbose mode
```

## Quickstart

1. You will need [python3](https://www.python.org/downloads/), [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), and [make](https://lmgtfy.com/?q=how+to+install+make) installed on your machine
2. Run some commands:

	```shell
	# Clone this repo
	git clone git@github.com:binarybeard/ingredient2recipe.git
	
	# Run make to install all the dependicies
	make
	```

3. Get an API Key from [food2fork](http://food2fork.com)
4. Run the program:

	```shell
	# Example (reaplce KEY with your API Key)
	python src/main.py --key KEY fish chicken
	
	# Get some verbosity
	python src/main.py --key KEY fish chicken --verbose
	
	# Use the mock json files (don't make API Calls)
	python src/main.py fish chicken --dev
	```
	
## Configuration File

To avoid using the `--key KEY` flag on the command line, put the API Key in `REPO_ROOT/config.json` file (REPO_ROOT is the root level of the cloned directroy). 

```json
{
	"api_key": "YOUR_API_KEY"
}
```

## Known Issues

As python is not my primary langague, there may be a lot of issues with the structure of the code. I ran into a few things when it came to building the tests...

### Ingredients names that are more than one word

**Example**

```
python src/main.py fish sauce
```

**Expected**

`['fish sauce']`

**Actual**

`['fish','sauce']`

**Fix**

Probably changing the delimiter to something other than whitespace. Using commas, or pipes, or something would be better, but not as user friendly.

**Estimation**

Easy, 30 minutes


### Sometimes ingredients only match the title

**Example**

```
python src/main.py cat
```

**Fix**

Parse through the recipes to ensure we are matching ingredients. This will also bring in the logic of paging through the API.

**Estimation**

Easy, 2 hours

### Fully qualified ingredient names

**Example**

```
python src/main.py fish chicken
```

**Fix**

We would need a better way to qualify ingredients. Chicken is very generic and isn't used in many recipes. Typically recipes call for chicken breast, or chicken thighs, etc. We need a better way to qualify the type of chicken [read: and other generic ingredients] the user is inputting. There would be a robust infrastructure of regular expressions to handle most of this logic.

**Estimation**

Medium, 1 day
