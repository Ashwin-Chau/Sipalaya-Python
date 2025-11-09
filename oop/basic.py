#Programming paradigms support by python:

#procedural programming : variable,function,loop
#functional programming : focus on function rather object == list(map(lambda))
#decalarative : focus on achievement/answer eg:- list comprehension
#OOP : it organize all model in object

# OOP :- variable is also object
# a=[1,2,3,4,5]
# name="sujan"
# age=45

# name1="ram"

# ----> student information
# r1 ----> name,age,phone 
# r2 ----> name,age,phone 

#OOP : Object Oriented Programming
#it map in real world sceanarios
#it match our variable in real world concept
#python use class and object to represent real world concept


#class : blueprint of object, template of creating object
#object : instance of class


#class is group of attribute and method

#attribute : it represent variable that contain the value/data
#method : it is similar to function that perform specific task

'''
syntax :

class ClassName:
    #class

ob=ClassName()
'''

#class ---> reserved keyword, Student ---> className
# class Student:
#     def __init__(self): #init --> it is special type of method which is used to initialize value into variable
#         self.name="sujan"   #attribute
#         self.age=45 #attribute

#     def show(self): #method
#         print(f"my name is {self.name}")

# ob=Student() #object
# ob2=Student()
# # ob.show()
# # print(ob.name)



# class Student:
#     def __init__(self,name,age): #init --> it is special type of method which is used to initialize value into variable
#         self.name=name   #attribute
#         self.age=age #attribute

#     '''self : it refer to the object : default variable that contain current object'''
#     def show(self): #method
#         print(f"my name is {self.name}")
#         print(f"my age is {self.age}")

# R1=Student("sujan", 66) #object
# R1.show()
# print(id(R1))

# R2=Student("ram",88)
# R2.show()
# print(id(R2))

# every time we create an object it allocating new space 



#attribute : product_name,qty,price
# method : total_price
# class Shop:
#     def __init__(self,name,qty,price):
#         self.name=name
#         self.qty=qty 
#         self.price=price 

#     def total_price(self):
#         total=self.qty*self.price 
#         print(f"Your product is {self.name} and total price is Rs,{total}")

# pen=Shop("pen",5,10)
# pen.total_price()

# book=Shop




#circle
#attribute : radius #do accept -ve value
#area, perimeter

# Answer in day12 task.py