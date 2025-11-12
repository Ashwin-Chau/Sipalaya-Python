#abstraction : the process of handing complexity by hiding unnecessary data form user and provide only service

# print("sujan")

# print(len("sujan"))

# def show(a,b):
#     print(a+b)

# show(2, 3)


# from hide import show

# show(3, 4)
# show(8, 8)


# abstract class : blueprint/template of other class

#abstract class ---> a class that contain one or more abstract method is called abstract class
#abstract method ----> a method that has declaration but doesnot have implementation
# we can't make object of abstract class it give error
# if we have only abstract method in a class we call it interface


# from abc import ABC,abstractmethod

# class A(ABC): #abstract class

#     @abstractmethod
#     def show(self):
#         pass

# class B(A):
#     def display(self):
#         print("hello world")

# ob=B()
# ob.display()


# from abc import ABC,abstractmethod

# class A(ABC): #abstract class

#     @abstractmethod
#     def show(self):
#         pass

# class B(A):
#     def display(self):
#         print("hello world")

#     def show(self):
#         print("this is show class")

# ob=B()
# ob.display()
# ob.show()

# class C(A):
#     def hello(self):
#         print("hello sipalaya")

#     def show(self):
#         print("show")

# ob=C()
# ob.hello()




# from abc import ABC,abstractmethod

# class A(ABC): #abstract class

#     @abstractmethod
#     def show(self):
#         pass

#     @abstractmethod
#     def register(self):
#         pass

# class B(A):
#     def display(self):
#         print("hello world")

#     def show(self):
#         print("this is show class")

#     def register(self):
#         print("successfully register")
# ob=B()
# ob.display()
# ob.show()




from abc import ABC,abstractmethod

class A(ABC): #abstract class

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def register(self):
        pass

    def main(self): #concrete method
        print("here some code")

class B(A):
    def display(self):
        print("hello world")

    def show(self):
        print("this is show class")

    def register(self):
        print("successfully register")
ob=B()
ob.display()
ob.show()
ob.main()