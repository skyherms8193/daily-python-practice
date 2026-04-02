"""
Kata: Multiply and Square

Description:
Create one function that multiplies two numbers and returns the result.
Create a second function that squares the result.

Then use both functions together to:
- multiply two numbers
- square the product

Concepts practiced:
- function definition
- parameters and arguments
- return values
- basic arithmetic
- using one function inside another

Notes:
This kata practices breaking a small problem into separate steps.
It also reinforces how the output of one function can be passed
into another function.

"""

def multi(n, m):
    return n * m

def square(result):
    return result ** 2


# Example usage
if __name__ == "__main__":
    print(square(multi(2, 3)))
