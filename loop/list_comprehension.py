#list comprehension : it is used to write the cleaner and shorter code in single line

#avoid : deep nested loop, multiple condition


#syntax : [expression for item in something]

# a=["sujan","ram","hari","dipendra"]

#len of each word

# op=[]

# for i in a:
#     op.append(len(i))

# print(op)


# op = [len(i) for i in a]
# print(op)


#if statement inside for loop 

# syntax : [expression for item in something if condition]

# a=["sujan","ram","hari","dipendra","syam"]

#name start with s
# op=[]

# for i in a:
#     if i.startswith("s"):
#         op.append(i)

# print(op)


# op=[i for i in a if i.startswith("s")]
# print(op)




#elif statement :

# synatx : ["true" if condition else "false" for item in something]

# a = [2,4,6,1,3,5,8]

# op=[]

# for i in a:
#     if i%2==0:
#         op.append("even")
#     else:
#         op.append("odd")

# print(op)

# op = ["even" if i%2==0 else "odd" for i in a]
# print(op)
