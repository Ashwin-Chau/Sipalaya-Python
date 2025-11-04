#function : block of code that perfrom some specific task whenever we call it 

#type of function :
#built in function :- pre-define or precodded by python
#print,len,max,min,str,int,range etc 

#user define function : these are function that you define by yourself using def keyword


'''
syntax:
def function_name():
    block of code (body of code)

function_name()   #calling function
'''

# def show():
#     print("hello ashiwn")
#     print("i want to learn django")


# print("----------------------")
# show()



# print("some imp code is here")


# show()





# def show():
#     a=2
#     b=3
#     c=a+b 
#     print("sum of two number is ",c)

# show()


'''
def function_name(formal argument):
    body of code

functio_name(actual argument)
'''

# def show(a,b):  #a,b is parameter
#     c=a+b 
#     print("sum of two number is ",c)
    
# show(2,3)
# show(33,7)



# return statement : it is used to exit a function and return or print some result


# def show(a):
#     print("sujan")
#     return a+2
    # print(a+2)
    # print("sujan")

# show(4)
# print(show(4))

#end the function  execution
#return show only when we print
#without any expression, then none value retrun


# a=[1,2,3,4]
# print(sum(a))

def show(a,b):
    return a+b 

print(show(2,3))