init:
	pip3 install -r requirements.txt

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean     to remove build fiels"
	@echo "  test      to run testing suite"
	@echo "  coverage  to check test coverage"

test:
	python3 -m pytest -vv tests/

coverage:
	coverage run src/main.py fish chicken --dev --verbose
	coverage run --source src -m py.test
	coverage combine
	coverage report --show-missing
	coverage html

clean:
	-rm -rf .coverage
	-rm -rf __pycache__
	-rm -rf src/__pycache__
	-rm -rf tests/__pycache__
	-rm -rf .pytest_cache
	-rm -rf htmlcov/

.PHONY: init test coverage
