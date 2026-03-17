"""
Kata: Basic Calculator

Description:
Create a function that takes two numbers and an operator (+, -, *, /)
and returns the result of the operation.

Concepts practiced:
- Conditional logic (if/elif/else)
- Function design
- Input validation
- Error handling

Notes:
Practicing how to map user input to specific program behavior
and handle edge cases like invalid operators and division by zero.
"""

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operator"


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    result = calculate(a, b, operator)
    print(f"Result: {a} {operator} = {result}")
