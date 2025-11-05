# iterator : object that contain countable number value(str,list,tuple,range,dict)

# a=[1,2,3,4,5]
# data=iter(a)
# print(next(data))
# print(next(data))


# three high order inbuilt function : function inside function but as a argument
#map(),filter(),reduce()

a=["sujan","zip","ram","hari"]
# print(max(a))

print(max(a,key=len))