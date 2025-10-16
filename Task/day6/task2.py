'''
Write a program to check if an input number is a multiple of 5 or not:
input=45
expected output = Yes
'''

number = int(input("Enter a number : "))

if number % 5 == 0:
    print(f"{number} is a multiple of 5")

else:
    print(f"{number} is not a multiple of 5")