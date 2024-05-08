from fuel import convert, gauge
import pytest

def test_ef():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"

def test_convert():
    assert convert("4/5") == 80
    assert convert("0/3") == 0

def test_errors():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")