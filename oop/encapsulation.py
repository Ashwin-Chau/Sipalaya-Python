#encapsulation : the process wrapping data(attribute) and method(function) with in single unit
# example is class

#main purpose :
# it is used to hide the data, protected data, control access of data

# to achieve encapsulation we use access modifier and property decorator

#access modifier : restrict variable and method access from globally by making private and protected

#accessor
#public accessor : attribute and methods are accessible from outside the class
#private accessor : attribute and method are accessible with only that class : __variable_name
#protected accessor : attribute and method are accessible only with in class and subclass : _variable_name


#public accessor : attribute and methods are accessible from outside the class
# class A():
#     def __init__(self):
#         self.name="sujan" 

#     def show(self):
#         print(f"my name is {self.name}")

# ob=A()
# # ob.show()
# # print(ob.name)

# class B():
#     def display(self):
#         print("this is display data",ob.name)

# b=B()
# b.display()




#private accessor : attribute and method are accessible with only that class : __variable_name
# class A():
#     def __init__(self):
#         self.__name="sujan" #private variable

#     def __show(self): #private method
#         print(f"my name is {self.__name}")

#     def display(self):
#         self.__show()

# ob=A()
# # print(ob.__name)
# # ob.__show()
# # ob.display()

# class B():
#     def display(self):
#         print("this is display data",ob.__name)

# b=B()
# b.display()




# class A():
#     def __init__(self):
#         self.__name="sujan" #private variable

#     def __show(self): #private method
#         print(f"my name is {self.__name}")

#     def display(self):
#         self.__show()

# ob=A()
# print(ob.__dict__)
# print(ob._A__name)



#protected accessor : attribute and method are accessible only with in class and subclass : _variable_name

# class A():
#     def __init__(self):
#         self._name="sujan" #protected variable

#     def show(self):
#         print(f"my name is {self._name}")

# ob=A()

# class B():
#     def display(self):
#         print("this is display data",self._name)

# b=B()
# b.display()





# class A():
#     def __init__(self):
#         self._name="sujan" #protected variable

#     def show(self):
#         print(f"my name is {self._name}")

# ob=A()

# class B(A):
#     def display(self):
#         print("this is display data",self._name)

# b=B()
# b.display()




# class A():
#     def __init__(self):
#         self._name="sujan" #protected variable

#     def show(self):
#         print(f"my name is {self._name}")

# ob=A()
# print(ob._name)




#property decorator : it allow you to access method like attribute

# class A():
#     def __init__(self):
#         self.__name="sujan"

#     @property
#     def show(self):
#         print(f"okey its me {self.__name}")

# ob=A()
# ob.show




# class A():
#     def __init__(self):
#         self.__name="sujan"

#     @property
#     def show(self):
#         print(f"okey its me {self.__name}")

#     @show.setter
#     def show(self,value):
#         self.__name=value

# ob=A()
# ob.show="ram"
# ob.show




# class A():
#     def __init__(self):
#         self.__name="sujan"

#     @property
#     def show(self):
#         print(f"okey its me {self.__name}")

#     @show.setter
#     def show(self,value):
#         self.__name=value

#     @show.deleter
#     def show(self):
#         del self.__name

# ob=A()
# del ob.show
# ob.show



# ---> Circle
# ob.radius (property decorator) -- 45
# ob.radius=10
#on.area


class Circle():
    def __init__(self):
        self.__radius=7

    @property
    def radius(self):
        print(f"Radius is {self.__radius}")

    @radius.setter
    def radius(self,value):
        if value>0:
            self.__radius=value
        else:
            raise ValueError("radius cannot be negative")

    @property
    def area(self):
        a=(3.14*(self.__radius**2))
        print(f"Area of circle is : {a}")

ob=Circle()
ob.radius = 11
ob.area