"""
Kata: Break Camel Case

Description:
Complete the function so that it inserts a space before each uppercase
letter in a string written in camelCase.

Examples:
"heyThere" -> "hey There"
"identifier"  -> "identifier"
""            -> ""

Concepts practiced:
- Iterating through strings
- String methods (isupper)
- Building strings dynamically
- Conditional logic

Notes:
Practicing how to detect uppercase letters and modify a string
based on character patterns. Reinforces building a new string
instead of modifying the original.
"""

def solution(s):
    words = ""
    for i in s:
        if i.isupper():
            words += " "
        words += i
    return words


# Example usage
if __name__ == "__main__":
    print(solution("heyThere"))  # hey There
