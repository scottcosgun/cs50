from plates import is_valid

def test_wrongnum():
    assert is_valid("ABCDEFG") == False
    assert is_valid("A") == False
    assert is_valid("AA") == True

def test_intstart():
    assert is_valid("123456") == False
    assert is_valid("AA01") == False

def test_nummid():
    assert is_valid("AA33AA") == False
    assert is_valid("AAA33") == True

def test_punct():
    assert is_valid("AA43!") == False
    assert is_valid("A A A") == False