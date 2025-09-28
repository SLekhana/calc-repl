import pytest
from calculator.cli import parse_numbers

def test_valid_numbers():
    a,b = parse_numbers(["3","4"])
    assert a==3.0 and b==4.0

def test_valid_floats():
    a,b = parse_numbers(["1.5","2.25"])
    assert a==pytest.approx(1.5) and b==pytest.approx(2.25)

def test_wrong_count():
    with pytest.raises(ValueError): parse_numbers(["1"])
    with pytest.raises(ValueError): parse_numbers(["1","2","3"])

def test_invalid_numbers():
    with pytest.raises(ValueError): parse_numbers(["a","b"])
    with pytest.raises(ValueError): parse_numbers(["1","two"])
