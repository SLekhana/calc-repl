import pytest
from calculator.operations import perform_operation, normalize_operation

@pytest.mark.parametrize(
    "op,a,b,expected",
    [("add",1,2,3),("+",1.5,2.5,4.0),("sub",5,3,2),("-",2,5,-3),
     ("mul",2,3,6),("*",-1,-4,4),("div",8,2,4),("/",9,3,3)],
)
def test_perform_operation_valid(op,a,b,expected):
    assert perform_operation(op,a,b) == pytest.approx(expected)

def test_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        perform_operation("div",1,0)

def test_unknown_operation_raises():
    with pytest.raises(ValueError):
        perform_operation("pow",2,3)

def test_normalize_operation_aliases():
    assert normalize_operation("PLUS") == "add"
    assert normalize_operation("-") == "-"
    assert normalize_operation("times") == "mul"
    assert normalize_operation("/") == "/"

def test_normalize_operation_unknown():
    with pytest.raises(ValueError):
        normalize_operation("weird")
