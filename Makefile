init:
	  pip install -r requirements.txt

test:
	  py.text tests

.PHONY: init test
