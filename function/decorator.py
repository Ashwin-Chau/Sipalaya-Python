# decorator : it is a function that takes another function as argument, add(function/features) and return in a new function 
# without changing origin 

# def outer(func):
#     def inner():
#         print("this is inner function")

#     return inner

# def show():
#     print("this is argument function")

# show() #this is argument function



# def outer(func): #show
#     def inner():
#         print("this is inner function")
#         func() #show()

#     return inner

# @outer
# def show():
#     print("this is argument function")

# show() #this is inner function,  #this is argument function




# def outer(func):
#     def inner():
#         print("this is inner function")
#         func()

#     return inner

# @outer
# def show():
#     print("this is argument function")

# # show()

# def display():
#     print("this is testing")

# display() #this is testing





# def outer(func): #display
#     def inner():
#         print("this is inner function")
#         func() #display()

#     return inner

# @outer
# def show():
#     print("this is argument function")

# # show()

# @outer
# def display():
#     print("this is testing")

# display() #this is inner function, #this is testing







#step 1:
# def show():
#     print("hello world")

# print(show()) #hello world, #None


# def show():
#     print("hello world")
#     return 

# print(show()) #hello world, #None


# def show():
#     print("hello world")
#     return "sujan"

# print(show()) #hello world, #sujan




#step 2 : everything is object in python
# def show():
#     print("hello")

# var=show 
# var()




# step 3 : nested function

# def outer():
#     print("this is outer function")

#     def inner():
#         print("this is inner function")

#     inner()

# outer()




# step 4 : a function can take another as argument
# def outer(func): #func=show
#     print("this is outer function")

#     def inner():
#         print("this is inner function")
#         func() #show()

#     inner()

# def show():
#     print("this is argument function")

# outer(show)





#decorator1
# def outer(func): #func=show
#     print("this is outer function")

#     def inner():
#         print("this is inner function")
#         func() #show()

#     return inner #var

# def show():
#     print("this is argument function")

# print("start")
# var = outer(show) #it assign in inner ---> inner = var
# print("okay")

# var()





#decorator2
# def outer(func): #func=show
#     print("this is outer function")

#     def inner():
#         print("this is inner function")
#         func() #show()

#     return inner #var

# @outer
# def show():
#     print("this is argument function")

# show()



def outer(func): #func=show
    print("going to be divide")

    def inner(a,b):
        if b==0:
            print("you cannot divide by zero")
            return
        func(a,b) 

    return inner #var

@outer
def show(a,b):
    print(a/b)

show(4,2)

@outer
def display(a,b):
    print(a/b)

display(7,0)