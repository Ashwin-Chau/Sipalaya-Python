'''
Write a Python function to multiply all the numbers in a list
'''

# def multiply():
#     l=[4,1,3,1,5,8,7,6,10]
#     mul = 1
#     for i in l:
#         mul *= i
#     print(f"Sum of all the number in list is {mul}")

# multiply()


l=[4,1,3,1,5,8,7,6,10]

def multiply(a):
    mul = 1
    for i in a:
        mul *= i
    print(f"Sum of all the number in list is {mul}")

multiply(l)