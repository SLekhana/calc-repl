def test_exit_message(monkeypatch):
    """Test that 'exit' prints the goodbye message and exits."""
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    outputs = []
    monkeypatch.setattr("builtins.print", outputs.append)

    import pytest
    from calculator import cli

    with pytest.raises(SystemExit):
        cli.main()
    
    # Check that the goodbye message was printed
    assert any("Goodbye!" in o for o in outputs)
