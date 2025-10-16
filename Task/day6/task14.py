'''
Write a program to check wheather character is vowel or not
'''

chracter = input("Enter a character : ")

vowel_letters = ['a','e','i','o','u']

if chracter.lower() in vowel_letters:
    print("It is vowel")

else:
    print("It is not vowel")