"""
Kata: String to Array

Description:
Convert a string into an array of words.

Notes:
- Words are separated by spaces.
- An empty string should return [''] (not an empty list).

Concepts practiced:
- String methods
- split() behavior
- Edge cases with empty strings

Example usage:
string_to_array("Robin Singh") ➞ ["Robin", "Singh"]
string_to_array("I love arrays") ➞ ["I", "love", "arrays"]
string_to_array("") ➞ [""]
"""

def string_to_array(s):
    return s.split(" ")


# Example runs
print(string_to_array("Robin Singh"))
print(string_to_array("I love arrays"))
print(string_to_array(""))
