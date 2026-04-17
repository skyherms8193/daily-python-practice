"""
Kata: Alternating Case

Description:
Define a function that switches the case of each letter in a string:
- Lowercase letters become uppercase
- Uppercase letters become lowercase
- Non-alphabetical characters remain unchanged

Examples:
"hello world" -> "HELLO WORLD"
"HELLO WORLD" -> "hello world"
"hello WORLD" -> "HELLO world"
"HeLLo WoRLD" -> "hEllO wOrld"
"12345" -> "12345"
"1a2b3c4d5e" -> "1A2B3C4D5E"

Concepts practiced:
- String iteration
- Conditional logic (if / elif / else)
- String methods (.islower(), .isupper(), .upper(), .lower())
- Building and returning new strings (immutability)

Notes:
- Strings in Python are immutable, so we build a new string instead of modifying the original
- The function is pure (does not mutate the input)
- Non-alphabetical characters must be preserved as-is
"""

def to_alternating_case(string):
    alt_string = ''
    for i in string:
        if i.islower():
            alt_string += i.upper()
        elif i.isupper():
            alt_string += i.lower()
        else:
            alt_string += i
    return alt_string


# Example usage:
if __name__ == "__main__":
    print(to_alternating_case("hello world"))        # "HELLO WORLD"
    print(to_alternating_case("HELLO WORLD"))        # "hello world"
    print(to_alternating_case("hello WORLD"))        # "HELLO world"
    print(to_alternating_case("HeLLo WoRLD"))        # "hEllO wOrld"
    print(to_alternating_case("12345"))              # "12345"
    print(to_alternating_case("1a2b3c4d5e"))         # "1A2B3C4D5E"
