'''
Write a Python function to find the maximum of three numbers.
'''


# def maximun():
#     a = 2
#     b = 3
#     c = 1
#     if a > b and b > c:
#         print(f"{a} is maximun")

#     elif b > c:
#         print(f"{b} is maximum")

#     else:
#         print(f"{c} is maximum")

# maximun()




def maximun(a,b,c):
    if a > b and a > c:
        print(f"{a} is maximun")

    elif b > c:
        print(f"{b} is maximum")

    else:
        print(f"{c} is maximum")

maximun(5,9,3)
maximun(5,2,3)
maximun(5,9,30)