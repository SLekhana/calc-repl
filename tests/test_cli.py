import builtins
import pytest
from calculator import cli

def run_cli_with_inputs(monkeypatch, inputs):
    """Helper to simulate user input and capture printed output."""
    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(it))

    outputs = []

    # Capture only printed strings
    monkeypatch.setattr(
        "builtins.print", 
        lambda *args, **kwargs: outputs.append(" ".join(map(str, args)))
    )

    with pytest.raises(SystemExit):  # main() exits on 'exit'
        cli.main()

    return outputs

def test_addition(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["add", "2", "3", "exit"])
    assert any("Result: 5.0" in o for o in outputs)

def test_subtraction(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["subtract", "5", "3", "exit"])
    assert any("Result: 2.0" in o for o in outputs)

def test_multiplication(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["multiply", "2", "4", "exit"])
    assert any("Result: 8.0" in o for o in outputs)

def test_division(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["divide", "8", "2", "exit"])
    assert any("Result: 4.0" in o for o in outputs)

def test_divide_by_zero(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["divide", "4", "0", "exit"])
    assert any("Cannot divide by zero" in o for o in outputs)

def test_invalid_operation(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["foobar", "exit"])
    assert any("Invalid operation. Try again." in o for o in outputs)
