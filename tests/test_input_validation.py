# tests/test_input_validation.py

import builtins
import pytest
from calculator import cli

def run_cli_with_inputs(monkeypatch, inputs):
    """
    Helper to simulate user input and capture printed output.
    `inputs` is a list of strings the user would type.
    """
    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(it))
    outputs = []
    monkeypatch.setattr("builtins.print", outputs.append)
    with pytest.raises(SystemExit):  # main() exits on 'exit'
        cli.main()
    return outputs

def test_invalid_number(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["add", "foo", "3", "exit"])
    assert any("Invalid number" in o for o in outputs)

def test_another_invalid_number(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["multiply", "5", "bar", "exit"])
    assert any("Invalid number" in o for o in outputs)

def test_empty_input(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["add", "", "3", "exit"])
    assert any("Invalid number" in o for o in outputs)

def test_multiple_invalid_inputs(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["subtract", "foo", "bar", "exit"])
    assert any("Invalid number" in o for o in outputs)
