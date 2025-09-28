from typing import Literal

Operation = Literal["add", "sub", "mul", "div", "+", "-", "*", "/"]

def perform_operation(op: Operation, a: float, b: float) -> float:
    if op in ("add", "+"):
        return a + b
    if op in ("sub", "-"):
        return a - b
    if op in ("mul", "*"):
        return a * b
    if op in ("div", "/"):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    raise ValueError(f"Unsupported operation: {op!r}")

def normalize_operation(token: str) -> Operation:
    t = token.strip().lower()
    mapping = {
        "add": "add", "+": "+", "plus": "add",
        "subtract": "sub", "sub": "sub", "-": "-", "minus": "sub",
        "multiply": "mul", "mul": "mul", "*": "*", "times": "mul",
        "divide": "div", "div": "div", "/": "/",
    }
    if t in mapping:
        return mapping[t]
    raise ValueError(f"Unknown operation: {token!r}")
