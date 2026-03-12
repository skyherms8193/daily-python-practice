"""
Kata: Square Every Digit

Description:
Square every digit of a number and concatenate the results.

Examples:
9119 -> 811181
765  -> 493625

Concepts practiced:
- Iterating through digits of a number
- String conversion
- Concatenation
- Basic arithmetic operations

Notes:
Practicing converting numbers to strings for iteration and rebuilding
a number from concatenated results.
"""

def square_digits(num):
    result = ""
    for digit in str(num):
        result += str(int(digit)**2)
    return int(result)

# Example usage
if __name__ == "__main__":
    print(square_digits(9119))  # 811181
    print(square_digits(765))   # 493625
