"""
Kata: Reverse Words

Description:
Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained exactly as they are.

Examples:
"Hello world"        -> "olleH dlrow"
"double  space"      -> "elbuod  ecaps"
" leading"           -> " gnidael"
"trailing "          -> "gniliart "

Concepts Practiced:
- String slicing
- Lists and list comprehensions
- String splitting and joining
- Handling edge cases (multiple spaces)

Notes:
- Using split(" ") instead of split() is important to preserve exact spacing.
- Each word is reversed individually, but word order stays the same.
"""

def reverse_words(text):
    words = text.split(" ")  # preserves exact spacing
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


# Example usage
if __name__ == "__main__":
    print(reverse_words("Hello world"))       # "olleH dlrow"
    print(reverse_words("double  space"))     # "elbuod  ecaps"
