#argument : an argument is a value that is passed to function when we call it

#type of argument
#positional argument
#keyword argument
#default argument
#arbitary argument


# def show(name):
#     print(f"my name is {name}")

# show("ashwin")
# show("ash")




#positional argument
# def show(name, age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")

# show("ram", 88)





#keyword argument
# def show(name, age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")

# show(age=22, name="sab")



#default argument :- it is should be at last
# def show(name, age, school="mangala"):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
#     print(f"school name is {school}")

# show("ram", 88)
# show("syam", 66, "united")





#arbitary argument : variable length
#positinal arbitary argument :- an argument prefix with a single astrisk(*)

# def show(*a):
#     print(a)
#     for i in a:
#         print(i)

# show(1,2,3,4,5)


#keyword arbitary argument

# def show(**a):
#     print(a)
#     for i,j in a.items():
#         print(i,j)


# show(name="sujan",age=99,email="ashiwn@gmail.com")



# def show(*a,**b):
#     print(a)
#     for i,j in b.items():
#         print(i,j)


# show(1,2,3,4,name="sujan",age=99,email="ashiwn@gmail.com")


