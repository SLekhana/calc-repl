from typing import Tuple, List
from calculator.operations import perform_operation, normalize_operation

def parse_numbers(tokens: List[str]) -> Tuple[float, float]:
    if len(tokens) != 2:
        raise ValueError("Please enter exactly two numbers.")
    try:
        a = float(tokens[0]); b = float(tokens[1])
    except ValueError:
        raise ValueError("Both inputs must be numbers.")
    return a, b

def process_command(op_token: str, num_tokens: List[str]) -> float:
    op = normalize_operation(op_token)
    a, b = parse_numbers(num_tokens)
    return perform_operation(op, a, b)

def print_help() -> None:
    print("Simple calculator REPL commands:")
    print("  add | +  : addition")
    print("  sub | -  : subtraction")
    print("  mul | *  : multiplication")
    print("  div | /  : division")
    print("  quit | q : exit")

def run_repl() -> None:
    print("Welcome to the calculator. Type 'help' for commands.")
    while True:
        try:
            raw_op = input("Operation: ").strip()
            if raw_op.lower() in ("quit","q","exit"):
                print("Goodbye."); break
            if raw_op.lower() in ("help","h","?"):
                print_help(); continue
            raw_nums = input("Enter two numbers separated by space: ").split()
            try:
                result = process_command(raw_op, raw_nums)
            except Exception as e:
                print(f"Error: {e}"); continue
            print(f"Result: {result}")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting."); break

if __name__ == "__main__":
    run_repl()
