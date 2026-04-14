"""
Kata: Exes and Ohs

Description:
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any character.

Concepts practiced:
- String methods (.lower(), .count())
- Conditional logic
- Boolean returns

Notes:
- Convert the string to lowercase to ensure case insensitivity
- Compare the counts of 'x' and 'o'
- If both counts are equal, return True; otherwise, return False
"""

def xo(s):
    s_lower = s.lower()
    return s_lower.count('x') == s_lower.count('o')


# Example usage
if __name__ == "__main__":
    print(xo("xo"))        # True
    print(xo("xxOo"))      # True
    print(xo("xxxm"))      # False
    print(xo("Oo"))        # False
    print(xo("ooom"))      # False
