# iterator : object that contain countable number value(str,list,tuple,range,dict)

# a=[1,2,3,4,5]
# data=iter(a)
# print(next(data))
# print(next(data))


# three high order inbuilt function : function inside function but as a argument
#map(),filter(),reduce()

# a=["sujan","zip","ram","hari"]
# # print(max(a))

# print(max(a,key=len))


#map(): its applies a function to each item of iterable , lazy operation 
#syntax : map(function, iterator)

# a=4
# def show(a):
#     return a+2

# print(show(a))


# a=[1,2,3,4,5]
# def show(a):
#     return a+2

# var = map(show,a)
# print(list(var))


# n=[1,2,3,4,5]
# v = lambda a:a*a
# var=map(v,n)
# print(list(var))


# n=[1,2,3,4,5]
# var=list(map(lambda a:a*a,n))
# print(var)



# filter() ----> filter item based on the function that return true/false

# n=[1,2,3,4,5] 

# def show(a):
#     return a%2==0

# var=filter(show,n)
# print(list(var))



# var=list(filter(lambda a:a%2==0,n))
# print(var)



# a=["sujan","ram","manoj","syam"]

# var=list(filter(lambda a:a.startswith("s"),a))
# print(var)



# reduce : applies a function to reduce is single value
# a = [1,2,3,4,5]

# from functools import reduce 
# def show(x,y): #x=1,y=2  ----> 3+3 ------> 6+4 -----> 10+5 ------>15
#     return x+y 

# var=reduce(show,a)
# print(var)