from calculator import operations

def test_add():
    assert operations.add(2, 3) == 5

def test_subtract():
    assert operations.subtract(5, 3) == 2

def test_multiply():
    assert operations.multiply(4, 2) == 8

def test_divide():
    assert operations.divide(8, 2) == 4

def test_divide_by_zero():
    try:
        operations.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
