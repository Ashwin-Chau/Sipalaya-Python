'''
Write a Python program to print the even numbers from a given list.
'''

# def even():
#     l=[4,1,3,1,5,8,7,6,10]
#     output = []
#     for i in l:
#         if i % 2 == 0:
#             output.append(i)
#     print(output)

# even()




l=[4,1,3,1,5,8,7,6,10]

def even(num):
    output = []
    for i in num:
        if i % 2 == 0:
            output.append(i)

    print(output)

even(l)