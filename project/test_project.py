from project import get_level, get_word, scramble, play, get_def, try_again
import random
from PyDictionary import PyDictionary
from io import StringIO

def test_get_word():
    assert len(get_word(4)) == 4
    assert len(get_word(1)) == 1
    assert len(get_word(12)) == 12

def test_scramble():
    word = get_word(random.randint(1,15))
    scrambled = scramble(word)
    letters = []
    for _ in scrambled:
        letters.append(_)
    for letter in word:
        assert letter in letters

def test_get_def():
    dictionary=PyDictionary()
    assert get_def("word") == dictionary.meaning("word")
    assert get_def("apple") == dictionary.meaning("apple")
