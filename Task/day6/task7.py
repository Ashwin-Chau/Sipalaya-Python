'''
Write a Python program to create a simple calculator that takes two numbers (num1 and num2) and an operator (+, -, *, /) as input from the user.
 Perform the corresponding operation based on the given operator using elif statements
'''

num1 = int(input("Enter first number : "))
operator = input("Enter (+, -, *, /) according to your needs : ")
num2 = int(input("Enter second number : "))


if operator == "+":
    print(f"Sum of {num1} and {num2} is {num1+num2}")

elif operator == "-":
    print(f"Subtract of {num1} and {num2} is {num1-num2}")

elif operator == "*":
    print(f"Multiply of {num1} and {num2} is {num1*num2}")

elif operator == "/":
    print(f"Division of {num1} and {num2} is {num1/num2}")

else:
    print("Enter a given operator")