'''
Write a Python program that takes a user's age as input and checks whether they are eligible to vote 
or not. The voting age is 18 years or older

input=20
ouput=You are eligible to vote.
'''

age=int(input("Enter your age : "))

if age >= 18:
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")