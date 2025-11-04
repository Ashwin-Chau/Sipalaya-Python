'''
Write a Python function to calculate the factorial of a number
'''

# def factorial():
#     num = 6
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i

#     print(f"Factorial of {num} is {fact}")

# factorial()



def factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact *= i 

    print(f"Factorial of {a} is {fact}")


factorial(5)        
factorial(6) 