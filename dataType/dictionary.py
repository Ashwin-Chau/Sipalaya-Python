#map : collection of data items (data structure) that have key-value pair, mutable, order(after 3.7 version), don't allow duplicate value

# a={
#     "name":["ashwin","bikas","mama"],
#     "age":22
# }

# var=dict(name="ashwin",age=22)
# print(type(a))
# print(a)

# print(len(a))

# print(a['name']) #if key value don't match it give error
# print(a.get("age","data not found")) 
# print(a.keys())
# print(a.values())
# print(a.items())

# a={
#     "name":"ashwin",
#     "age":22,
# }

# a.setdefault("address","chit")
# print(a)

# a["address"]="chitwan"

# b={
#     "email":"ash@gmail.com",
#     "age":23
# }
# a.update(b)

# a.pop("age")
# a.popitem() # used to remove last pair value

# print(a)



# a=["ashiwn","hari","sab"]

# var=dict.fromkeys(a,"present")
# var['hari']="absent"
# print(var)