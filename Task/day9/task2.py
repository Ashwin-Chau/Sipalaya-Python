
'''
Write a Python function to sum all the numbers in a list.
'''


# def sum():
#     l=[4,1,3,1,5,8,7,6,10]
#     total = 0
#     for i in l:
#         total += i
#     print(f"Sum of all the number in list is {total}")

# sum()




l=[4,1,3,1,5,8,7,6,10]

def sum(a):
    total = 0
    for i in a:
        total += i
    print(f"Sum of all the number in list is {total}")

sum(l)
