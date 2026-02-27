"""
Kata: Even or Odd

Description:
Return "Even" if a number is even, otherwise return "Odd".

Concepts practiced:
- Modulo operator
- Conditional logic
- Return statements

Notes:
Practicing writing simple conditionals cleanly and avoiding unnecessary complexity.
"""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Example usage
if __name__ == "__main__":
    print(even_or_odd(4))  # Even
    print(even_or_odd(7))  # Odd
