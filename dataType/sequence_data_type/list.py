#list : list is collection of data items(data structure) which is mutable
# (changable),order and allow duplicate value

# a=["ashiwn",77,23.99,True]
# a=["ashiwn","hari","dipak"]

# print(type(a))
# print(len(a))

# print(a[0])
# print(a[2:4])
# a[0]="ram"

# a.append("junge")
# a.extend(["junge","plp"])
# a.insert(1,"hari")
# a.clear()
# del a
# a.pop(1)
# print(a)

# a=[4,5,2,1,3,6]

# # a.sort(reverse=True) #sort change on original list
# # print(a)

# b=sorted(a,reverse=True) #sorted make a new location to store and change in it not in the original list
# print(b)
# print(a)

# b=a #refrence
# b=a.copy() #copy

# shallow copy and deep copy
# import copy
# a=["ram",2,3,[11,33]]
# b=a.copy()

# a[3].append("sujan")

# print(b) #['ram', 2, 3, [11, 33, 'sujan']]
# print(a) #['ram', 2, 3, [11, 33, 'sujan']]

#deep copy
# b=copy.deepcopy(a)
# a[3].append("sujan")
# print(b)
# print(a)

# a.append("ash")
# print(a)
# print(b)


#nested list : one list inside another list
# a=[1,2,3,4,["ashiwn","hari"]]

# print(a[4])
# v=a[4][0]
# print(v)
# print(type(v))


# a=["ashiwn","ram","hari","manoj"]
# print(a)
# v=" ".join(a)
# print(v)
# print(type(v))