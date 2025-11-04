#variable : reserved memory location 
#type of variable
#local variable :- a variable which is declare inside the function
#global varibale :- a variable which is declare outside the function

# course="python"
# course="django"
# print(course)


# course="python"          #global varibale :- a variable which is declare outside the function
# def show():
#     course="django"     #local variable :- a variable which is declare inside the function
#     print(course)

# show()
# print(course)



# a=30
# def show():
#     v=40
#     print(v, "calling local variable inside function")
#     print(a, "calling global variable inside function")

# show()

# print(a,"global variable outside function")



# a=20
# def show():
#     global a
#     a=a+1
#     print(a)
#     # b=a+1
#     # print(b)

# show()



# a=[1,2,3,4,5]
# b=0

# def show(var):
#     global b
#     for i in var:
#         b+=i
        
#     print(b)

# show(a)





#nested function : a function inside another function

# def outer():
#     print("this is outer function")

#     def inner():
#         print("this is inner function")

#     inner()
#     print("this is outer function")


# outer()


# def outer():
#     v=20
#     def inner():
#         nonlocal v
#         v+=1
#         print(v)

#     inner()

# outer()