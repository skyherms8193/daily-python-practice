"""
Remove the Smallest Value

Write a function that removes the smallest value from a list of integers.

Requirements:
- Do not mutate the original list
- If there are multiple occurrences of the smallest value, remove only the first one
- If the list is empty, return an empty list

Examples:
remove_smallest([1, 2, 3, 4, 5]) -> [2, 3, 4, 5]
remove_smallest([5, 3, 2, 1, 4]) -> [5, 3, 2, 4]
remove_smallest([2, 2, 1, 2, 1]) -> [2, 2, 2, 1]
remove_smallest([]) -> []

Concepts practiced:
- Lists
- Copying vs mutating data
- Built-in functions (min, remove)
- Conditional logic
"""

def remove_smallest(numbers):
    if not numbers:
        return []

    num = numbers.copy()  # avoid mutating original list
    num.remove(min(num))  # removes first occurrence of smallest value
    return num


# Example usage
if __name__ == "__main__":
    print(remove_smallest([1, 2, 3, 4, 5]))
    print(remove_smallest([5, 3, 2, 1, 4]))
    print(remove_smallest([2, 2, 1, 2, 1]))
    print(remove_smallest([]))
