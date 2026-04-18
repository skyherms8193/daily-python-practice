"""
Kata: Abbreviate a Two-Word Name

Description:
Convert a name into initials. This kata takes exactly two words with one space
in between them and returns two capital letters separated by a dot.

Examples:
"george washington" -> "G.W"
"frederick douglas" -> "F.D"

Concepts practiced:
- String splitting
- Indexing
- String formatting (f-strings)
- Uppercase conversion

Notes:
- Assumes input always contains exactly two words
- Output format must be "X.Y" (no trailing dot)
"""

def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"


# Example usage
if __name__ == "__main__":
    print(abbrev_name("george washington"))   # G.W
    print(abbrev_name("frederick douglas"))   # F.D
