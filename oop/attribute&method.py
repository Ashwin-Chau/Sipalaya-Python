#class ---> attribute and method

#type of attribute
#instance variable
#class variable/static variable

#type of method
#instance method
#class method
#static method


#instance variable : those variable whose separated copy of file created for every object 
#define and initialize using a constructor with 'self' parameter


# class Student:
#     def __init__(self,name):
#         self.name=name  #instance variable

#     def show(self): #instance method : those method that is used to access instance variable
#         print(f"my name is {self.name}")

# ob=Student("sujan")
# ob.name="hari"
# print(ob.name)
# # ob.show()

# ob2=Student("ram")
# print(ob2.name)
# ob2.show()



#class variable : those variable whose single copy file is create for every object
#define and initialize using a constructor with 'cls' parameter


# class Student:
#     school="mangala" #class variable
#     def __init__(self,name):
#         self.name=name  #instance variable

#     @classmethod
#     def show(cls):
#         print(f"my school name is {cls.school}")

# ob=Student("sujan")
# # ob.school="united"
# Student.school="united"
# # print(Student.school)
# print(ob.school)

# ob2=Student("syam")
# print(ob2.school)




#static method :- if we don't want to use both class and instance then only we use this

# class Student:

#     @staticmethod
#     def show():
#         print("hello world")

# ob=Student()
# ob.show()