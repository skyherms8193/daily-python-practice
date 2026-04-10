"""
Kata: Highest and Lowest

Description:
Given a string of space-separated numbers, return the highest and lowest number.

Notes:
- All numbers are valid integers
- There will always be at least one number
- Output should be a string with the highest number first, then the lowest, separated by a space

Examples:
high_and_low("1 2 3 4 5") → "5 1"
high_and_low("1 2 -3 4 5") → "5 -3"
high_and_low("1 9 3 4 -5") → "9 -5"

Concepts practiced:
- String splitting
- Type conversion (str → int)
- Lists and loops
- max() and min()
- f-strings

Notes:
- split() converts the string into a list of substrings
- Each element must be converted to an integer before using max() and min()
"""

def high_and_low(numbers):
    split_num = numbers.split(" ")
    nums = []

    for n in split_num:
        nums.append(int(n))

    return f"{max(nums)} {min(nums)}"


# Example usage
print(high_and_low("1 2 3 4 5"))      # "5 1"
print(high_and_low("1 2 -3 4 5"))     # "5 -3"
print(high_and_low("1 9 3 4 -5"))     # "9 -5"
