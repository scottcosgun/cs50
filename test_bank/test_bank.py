from bank import value

def test_hello():
    assert value("HELLO") == 0
    assert value("hello jake") == 0

def test_hey():
    assert value("HEY") == 20

def test_100():
    assert value("what's up?") == 100