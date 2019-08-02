import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src import main

def test_debug(capsys):
    main.debug('Hello World')
    captured = capsys.readouterr()
    assert captured.out == 'Hello World'
