"""
Kata: Remove the Smallest Value from a List

Description:
Write a function that removes the smallest value from a list
and returns the result as a new list.

If there are multiple occurrences of the smallest value,
remove only the first one.

If the list is empty, return an empty list.

Examples:
[1, 2, 3, 4, 5]      -> [2, 3, 4, 5]
[5, 3, 2, 1, 4]      -> [5, 3, 2, 4]
[2, 2, 1, 2, 1]      -> [2, 2, 2, 1]
[]                   -> []

Concepts practiced:
- Lists
- Conditional logic
- Built-in functions (min)
- Copying lists
- Removing elements safely

Notes:
Practicing how to work with lists without changing the original input.
Also reinforces handling edge cases like an empty list and removing
only the first occurrence of the smallest value.
"""

def remove_smallest(numbers):
    if not numbers:
        return []
    num = numbers.copy()
    num.remove(min(num))
    return num


# Example usage
if __name__ == "__main__":
    print(remove_smallest([1, 2, 3, 4, 5]))   # [2, 3, 4, 5]
    print(remove_smallest([5, 3, 2, 1, 4]))   # [5, 3, 2, 4]
    print(remove_smallest([2, 2, 1, 2, 1]))   # [2, 2, 2, 1]
    print(remove_smallest([]))                # []
