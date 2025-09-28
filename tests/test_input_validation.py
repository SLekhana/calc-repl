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

def test_invalid_numbers(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["add", "two", "three", "exit"])
    assert any("Invalid number entered." in o for o in outputs)

def test_divide_by_zero(monkeypatch):
    outputs = run_cli_with_inputs(monkeypatch, ["divide", "5", "0", "exit"])
    assert any("Cannot divide by zero" in o for o in outputs)
