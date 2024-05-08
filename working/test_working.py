from working import convert
import pytest

def test_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        assert convert("9 to 5")
        assert convert("9 - 5")

def test_midnight():
    assert convert("12 AM to 9 AM") == "00:00 to 09:00"
    assert convert("6:30 AM to 12:30 PM") == "06:30 to 12:30"
    assert convert("4:00 PM to 12:00 AM") == "16:00 to 00:00"

def test_numeric():
    with pytest.raises(ValueError):
        assert convert("cat")
        assert convert("C PM to D PM")

def test_without_to():
    with pytest.raises(ValueError):
        assert convert("9 AM 5 PM")

def test_out_of_range():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:00 PM")
        assert convert("9:00 AM to 13:00 PM")

def test_invalid_time_format():
    with pytest.raises(ValueError):
        assert convert("9-00 AM to 5-00 PM")