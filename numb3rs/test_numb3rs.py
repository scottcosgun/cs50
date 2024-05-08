from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3.4.") == False
    assert validate(".1.2.3.4") == False
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False

def test_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.256") == False
    assert validate("cat.2.3.4") == False
    assert validate("a.b.c.d") == False

if __name__ == "__main__":
    main()