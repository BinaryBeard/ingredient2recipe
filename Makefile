init:
	pip3 install -r requirements.txt

test:
	python3 -m pytest -vv tests/

coverage:
	coverage run --source src -m py.test
	coverage report --show-missing

.PHONY: init test coverage
