# 1. Which of the following is not a keyword in python language?
# a)eval
# b)assert
# c)nonlocal
# d)pass 
# Ans eval

# 2.what is output?
# a = [1,2,3]
# b=a
# b.append(4)
# print(a)
# a)[1,2,3]
# b)[1,2,3,4]
# c)[4,1,2,3]
# d)error
# Ans [1,2,3,4]

# 3. Which of the following operator is correct option for power(ab)?
# a)a^b
# b)a**b
# c)a.power(b)
# d)a^*b  
# # Ans a**b

# 4. what is a difference between == and is operator in Python? 
# a) == compares the values of two objects while is compares their memory address
# b) == compares the memory address of two objects while is compares values
# c) == is used for assignment while is is used for comparision
# d) == is used for identify testing while is used for value testing
# Ans a) == compares the values of two objects while is compares their memory address


# 5. Output?
# a,b = "23"
# b,c = "67"
# print(a+b+c)
# a)2367
# b)267
# c)237
# d)error
# Ans b)267


# 6. Choose the correct answer of print(12&13)?
# a)12
# b)13
# c)-13
# d)None
# Ans a)12

# 12 ---> 1100
# 13 ---> 1101
# =============
#         1100


# 7. What is the output of(2*3**3//4)?
# a)13
# b)18
# c)54
# d)12
# Ans a)13

# print(2*3**3//4) #----> 2*27//4 -----> 54//4 -----> 13



# 8. What will be output of the following code?
# a = 1
# while True:
#     if a % 7 == 0:
#         break
#     print(a)
#     a += 1
# a)1234567
# b)123456
# c)12345
# d)error
# Ans b)123456



# 9. Find Output
# y = 8
# z = lambda x:x*y
# print(z(6))
# a)Error
# b)48
# c)14
# d)None of these
# Ans b)48


# 10. When was Python first released?
# a)1985
# b)1991
# c)1995
# d)2000
# Ans b)1991



# 11. What is the output?
# print(0.1 + 0.2 == 0.3)
# a)True
# b)False
# c)Error
# d)None
# Ans b)False

# a = 0.3
# print(0.1 + 0.2) #0.30000000000000004



# 12. What happens when '2' == 2 is executed?
# a)True
# b)False
# c)ValueError occur
# d)type error
# Ans b)False


# 13. What will be the output
# data = {1 : 1, 2 : '2', '1' : 1, '2' : 3}
# data['1'] = 2
# print(data[data[data[str(data[1])]]])
# a)2
# b)3
# c)"2"
# d)Error
# Ans b)3


# data = {
#     1:1,
#     2:"2",
#     "1":1, #2
#     "2":3
# }
# data['1'] = 2
# print(data[data[data[str(data[1])]]]) #data[1] --> 1

# print(data[data[data[str(1)]]]) #data[str(1)] ---> 2
# print(data[data[2]])  #data[2] ----> "2"
# print(data["2"])  #data["2"] ----> 3




# 14. What will be the output?
# x = 10
# def outer():
#     x = 20
#     def inner():
#         nonlocal x 
#         x = 30
#     inner()
#     return x 
# print(outer())
# a)10
# b)20
# c)30
# d)Error
# Ans c)30



# 15. What will be the output?
# def show(x,y=[]):
#     y.append(x)
#     return y 
# print(show(1))
# print(show(2))
# a)[1][2]
# b)[1][1,2]
# c)[1,2][1,2]
# d)None
# Ans b)[1][1,2]


# def show(x,y=[]): #x=1, y=[1]
#                   #x=2, y=[1]
#     y.append(x)
#     return y #[1] [1,2]
# print(show(1))
# print(show(2))



# 16. What will be the output?
# import copy
# a = [[1,2],[3,4]]
# b = copy.deepcopy(a)
# a[0][0] = 99
# print(b[0][0])
# a)99
# b)1
# c)None 
# d)Error
# Ans b)1




# 17. What does a.get("name","default") return if "name" is not in the dictionary?
# a)Raised key Error
# b)None
# c)default
# d)An Empty String
# Ans c)default



# 18. Output of the following statement:
# Print("a"+"bc")
# a)a+b+c
# b)abc
# c)Error
# d)None
# Ans c)Error



# 19. What happens when False == 0 is executed?
# a)False
# b)True
# c)None
# d)Error
# Ans b)True



# 19. What is the syntax of slicing?
# a)variable_name[start,end,stop]
# b)variable_name[start:end:stop]
# c)variable_name(start,end,stop)
# d)variable_name(start:end:stop)
# Ansb)variable_name[start:end:stop]