'''
Write a Python program that:

Takes a sentence as input from the user

Counts and displays the number of words in the sentence
input="my name is sujan"
output="total word in sentence is 4"
'''

#taking input from user
sentence=input("Enter a sentence : ")

word=sentence.split()
total_words=len(word)
print(f"Total word in sentence is {total_words}")