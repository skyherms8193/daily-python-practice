"""
Kata: Word Count and Letter Count

Description:
Write a function that takes a sentence as input and:
- Returns the number of words in the sentence
- Prints each word along with the number of letters it contains

Concepts practiced:
- String input
- Splitting strings into lists
- Iterating through lists
- Using len() function
- Formatted string output (f-strings)

Notes:
Practicing basic string manipulation and iteration, which are foundational
skills for text processing tasks.
"""

sentence = input("Please enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))

for word in words:
    print(f'The word "{word}" has {len(word)} letters.')


# Example usage
if __name__ == "__main__":
    pass
