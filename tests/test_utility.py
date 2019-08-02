import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src import utility

def test_inform(capsys):
    utility.inform('Hello World')
    captured = capsys.readouterr()
    assert captured.out == '\x1b[1m\x1b[40m\x1b[35mHello World\n'

def test_get_json_file():
    test_json = utility.get_json_file('./mocks/mock_get.json')
    assert test_json['count'] == 1

def test_get_json_url():
    test_json = utility.get_json_url('http://xkcd.com/149/info.0.json')
    assert test_json['title'] == 'Sandwich'

def test_get_json_url_bad():
    test_json = utility.get_json_url('http://xkcd.com/abc/info.0.json')
    assert test_json['error'] == 'fatal'
