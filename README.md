# Interactive Calculator (REPL)

Run:
  python -m calculator.cli

Tests & coverage:
  pip install -r requirements.txt
  coverage run -m pytest
  coverage report -m
  coverage report --fail-under=100
