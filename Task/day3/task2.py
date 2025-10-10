'''
Task:
Write a Python program that takes a sentence as input and give a new string with the words 
in reverse order, while maintaining each word's original form.

Input:  "Hello World! Python is awesome"
Output: "awesome is Python World! Hello"

Input:  "SingleWord"
Output: "SingleWord"
'''

# take input
sentence=input("Enter a sentence: ")

# splitting the sentence
words=sentence.split()
print(type(words))

# reversed_sentence=sentence[::-1]
reversed_words=words[::-1]
reversed_sentence = ' '.join(reversed_words)

#output
print(reversed_sentence)
