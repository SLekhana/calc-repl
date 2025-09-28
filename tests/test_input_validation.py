import builtins
import pytest
from calculator import cli

def run_cli_with_inputs(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(it))
    outputs = []
    monkeypatch.setattr("builtins.print", outputs.append)
    with pytest.raises(SystemExit):
        cli.main()
    return outputs

def test_invalid_number(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["add", "foo", "bar", "exit"])
    assert any("Invalid number entered." in o for o in outputs)

def test_invalid_operation(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["foobar", "exit"])
    assert any("Invalid operation" in o for o in outputs)

def test_divide_by_zero(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["divide", "5", "0", "exit"])
    assert any("Cannot divide by zero" in o for o in outputs)
