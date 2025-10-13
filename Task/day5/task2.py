'''
String Manipulation & Tuple Conversion
Given the following string:
value = "python is high level programming language"
Write a Python program to:

Capitalize the first letter of each word

Split the string into individual words

Convert the result into a tuple of these capitalized words
OutPut =("Python", "Is", "High", "Level", "Programming","Language")
'''

value = "python is high level programming language"

capitalize_first = value.title()
print(capitalize_first)

splitting_word = capitalize_first.split()
print(splitting_word)

convert = tuple(splitting_word)
print(convert)