import pytest
from calculator.cli import process_command
from calculator.operations import perform_operation

def test_process_command_success():
    res = process_command("add",["2","3"])
    assert res == perform_operation("add",2.0,3.0)

def test_process_command_invalid_op():
    with pytest.raises(Exception):
        process_command("pow",["2","3"])

def test_process_command_invalid_numbers():
    with pytest.raises(Exception):
        process_command("add",["two","three"])
