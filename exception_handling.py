'''
exception_handling : it is the process of responding unexpected event when program is run / how to handle error

syntax:
try:
    block of code

except:
    error message

'''

# def show():
#     print(2+"2")

# show()

# print("some imp code is here....")




# try:
#     def show():
#         print(2+"2")

#     show()

# except:
#     print("some error is occur")

# print("some imp code is here....")





# try:
#     def show():
#         print(2+2)

#     show()

# except:
#     print("some error is occur")

# print("some imp code is here....")






'''
types of error :
compile time error :- error comes before run
logical error :- 



excention handling use to handle runtime error 
run time error :- error comes after run 
types of run type error :
TypeError
IndexError
ZeroDivisionError
KeyError
ValueError

'''

#compile time error
# print("sujan"
#  print("sujan")


#logical error
# def show(a,b):
#     print(a+b)

# show(2,3)


#run time error
# a={
#     "name":"sujan"
# }
# print("sujan"+2) #TypeError
# print("sujan"[10]) #IndexError
# print(4/0) #ZeroDivisionError
# print(a['age']) #KeyError
# print(int("sujan")) #ValueError



# try:
#     def show():
#         print(4/0)

#     show()
# except:
#     print("some error")




# try:
#     def show():
#         print(4/0)

#     show()
# except ZeroDivisionError:
#     print("value cannot divide by zero")
# except:
#     print("some error")




# try:
#     def show():
#         print("sujan"+2)

#     show()
# except ZeroDivisionError:
#     print("value cannot divide by zero")
# except TypeError:
#     print("different string and integer cannot be divide")
# except:
#     print("some error")




# try:
#     def show():
#         print(2+2)

#     show()
# except ZeroDivisionError:
#     print("value cannot divide by zero")
# except TypeError:
#     print("different string and integer cannot be divide")
# except:
#     print("some error")





# try:
#     def show():
#         # print("2"+2)
#         print(4/0)
#     show()
# except Exception as e:
#     print(f"Error {e}")




'''
try:
    code 
except:
    error message
finally:
    always executed
'''

#finally : always executed

# try:
#     def show():
#         print("hello world")
    
#     show()
# except:
#     print("error")
# finally:
#     print("some imp data or code here")





# try:
#     def show():
#         print("hello world")
    
#     show()
# except:
#     print("error")

# print("some imp data or code here")




# def show():
#     try:
#         print("hello this is working") 
#     except:
#         print("some error occur")
    
#     print("some imp code is  here")

# show()





# def show():
#     try:
#         print("hello this is working"[111]) 
#     except:
#         print("some error occur")
    
#     print("some imp code is  here")

# show()





# def show():
#     try:
#         print("hello this is working"[111]) 
#     except:
#         print("some error occur")
#         return 1
    
#     print("some imp code is  here")

# show()






def show():
    try:
        print("hello this is working"[111]) 
    except:
        print("some error occur")
        return 1
    
    finally:
        print("some imp code is  here")

show()