"""
Kata: Convert String to Camel Case

Description:
Complete the function so that it converts dash/underscore delimited words
into camel casing.

The first word within the output should be capitalized only if the original
word was capitalized. All following words should be capitalized.

Examples:
"hello-world" -> "helloWorld"
"Hello-world" -> "HelloWorld"
"python_is_fun" -> "pythonIsFun"
"Python-is_fun" -> "PythonIsFun"

Concepts practiced:
- String replacement
- Splitting strings
- Iterating through lists
- String capitalization
- Building a result string

Notes:
Practicing how to normalize different delimiters and transform a string
into camel case while preserving the original capitalization of the first word.
"""

def to_camel_case(text):
    text = text.replace("-", "_")
    words = text.split("_")
    
    result = words[0]
    
    for word in words[1:]:
        result += word.capitalize()
    
    return result


# Example usage
if __name__ == "__main__":
    print(to_camel_case("hello-world"))           # helloWorld
    print(to_camel_case("Hello-world"))           # HelloWorld
    print(to_camel_case("python_is_fun"))         # pythonIsFun
    print(to_camel_case("Python-is_fun"))         # PythonIsFun
