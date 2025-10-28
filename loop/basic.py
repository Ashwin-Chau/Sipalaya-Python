#loop: loop are use to repeat a instruction
#loop is programming structure that repeat a block of code multiple time base on condition or number of iteration


#types of loop :
#for loop :
# loop which is use to repeat for pre-determine number
# it is used for sequential traversal(list,str,tuple,dict,set,range etc.....)

#syntax


'''
for item in iterable:
    block of code
'''

# friends=["ashwin","ram","hari","manoj"]

# for i in friends:
#     # print(i)
#     # print(i, end=" ")
#     print("serving tea to",i)


# a = "ashiwn"
# a=(1,2,3,4,5)

# for i in a:
#     # print(i)
#     print("ashwin",i)



# a={
#     "name":"ashwin",
#     "age":22
# }

# for i in a:
# for i in a.items():
# for i,j in a.items():
    # print(i)
    # print(j)
    # print(i,j)



#range(start,end,step)

# for i in range(3,10):
#     print(i)

# for i in range(3,10,2): #3,5,7,9
#     print(i)


# for i in range(10,0,-1):
#     print(i)


# for i in range(10):
#     # print(i)
#     print("ashwin",i)


#multitlication table using for loop

'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
'''

# num = 2
# num = int(input("Enter your multiplication number : "))
# for i in range(1,11):
#     # print(i)
#     # print(num,i)
#     # print(num, "x",i, "=",num*i)
#     print(f"{num} x {i} = {num*i}")




#if statememnt inside for loop

# a=["ashwin","ram","hari","ash"]
# b=["ashwin","ash"]
# b=[]

# for i in a:
#     # print(i)
#     if i.startswith("a"):
#         # print(i)
#         b.append(i)

# print(b)


# a=[1,2,3,4,5,6,8]
# op=[2,4,6,8]
# op=[]

# for i in a:
#     if i % 2 == 0:
#         op.append(i)

# print(op)