from um import count

def test_upper():
    assert count("UM") == 1
    assert count("YUMMY") == 0

def test_lower():
    assert count("um") == 1
    assert count("um where am I?") == 1

def test_multiple():
    assert count("um um um um") == 4

def test_punctuation():
    assert count("um... why am I, um, even here?") == 2

def test_words():
    assert count("yummy") == 0