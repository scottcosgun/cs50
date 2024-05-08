from seasons import validate, minutes
from datetime import date

def test_validate():
    assert validate("2021-10-31") == date(2021, 10, 31)