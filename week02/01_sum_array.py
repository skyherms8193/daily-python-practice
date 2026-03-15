"""
Kata: Sum of an Array

Description:
Write a function that takes an array (list) of numbers and returns the sum
of those numbers.

The numbers may be positive or negative.

If the array is empty, the function should return 0.

Concepts practiced:
- Iterating through lists
- Using an accumulator variable
- Conditional checks for empty input
- Basic arithmetic operations

Notes:
Practicing how to process a list of values and maintain a running total.
This is a common foundational pattern in many programming problems.
"""

def sum_array(a):
    result = 0
    
    if len(a) == 0:
        return 0
    for i in range(len(a)):
        result += a[i]
    
    return result


# Example usage
if __name__ == "__main__":
    print(sum_array([1, 2, 3]))        # 6
    print(sum_array([10, -2, 5]))      # 13
    print(sum_array([]))               # 0
