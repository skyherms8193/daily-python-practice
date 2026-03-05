"""
Kata: Disemvowel Trolls

Goal:
Remove all vowels from a given string.

Concepts practiced:
- Iterating through characters
- String replacement
- Working with immutable strings
"""

def disemvowel(string: str) -> str:
    vowels = "aeiouAEIOU"

    for v in vowels:
        string = string.replace(v, "")

    return string


if __name__ == "__main__":
    print(disemvowel("Hello World"))   # Hll Wrld
    print(disemvowel("Skylar"))        # Skylr
