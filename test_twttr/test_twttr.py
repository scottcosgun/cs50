from twttr import shorten

def test_uppercase():
    assert shorten("DAVID") == "DVD"

def test_lowercase():
    assert shorten("david") == "dvd"

def test_vowels():
    assert shorten("aeiou") == ""

def test_numbers():
    assert shorten("123456") == "123456"

def test_punctuation():
    assert shorten("twitter!?@#") == "twttr!?@#"