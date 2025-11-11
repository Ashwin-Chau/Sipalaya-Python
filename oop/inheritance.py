#four fundamental concepts of oop:
#inheritance : class that inherit all method and attribute from another existing class

#base class ----> parent class/already exist class
#derived class ---> child class


# class A():
#     def show1(self):
#         print("I have a feature one ")

# ob=A()
# ob.show1()

# Types of inheritance
# single inheritance
# single level(multi-level inheritance)
# multiple inheritance
# hierachical inheritance
# hybrid inheritance



# single inheritance
# class A(): #parent class
#     def show1(self):
#         print("I have a feature one ")

# class B(A):
#     def show2(self):
#         print("I have a feature two")

# ob=B() #child class
# ob.show2()
# ob.show1()



# single-level/ multi-level inheritance
# class A(): #grand-parent class
#     def show1(self):
#         print("I have a feature one ")

# class B(A): #parent class
#     def show2(self):
#         print("I have a feature two")

# class C(B): #child class
#     def show3(self):
#         print("I have a feature three")

# ob=C() 
# ob.show3()
# ob.show2()
# ob.show1()




# multiple inheritance (mixin)
# class A(): #father
#     def show1(self):
#         print("I have a feature one")

# class B(): #mother
#     def show2(self):
#         print("I have a feature two")

# class C(A,B): #child 
#     def show3(self):
#         print("I have a feature three")

# ob=C()
# ob.show3()
# ob.show1()
# ob.show2()




# hierachical inheritance
# class A(): #parent
#     def show1(self):
#         print("I have a feature one")

# class B(A): #child
#     def show2(self):
#         print("I have a feature two")

# class C(A): #child
#     def show3(self):
#         print("I have a feature three")

# ob1=C()
# ob1.show3()
# ob1.show1()

# ob2=B()
# ob2.show2()
# ob2.show1()



# Hybrid Inheritance Example

class A:  # Parent class
    def show1(self):
        print("I have a feature one")

class B(A):  # Child of A
    def show2(self):
        print("I have a feature two")

class C(A):  # Another child of A
    def show3(self):
        print("I have a feature three")

# New class D inherits from both B and C
class D(B, C):
    def show4(self):
        print("I have a feature four")

# Creating objects
ob1 = C()
ob1.show3()
ob1.show1()

ob2 = B()
ob2.show2()
ob2.show1()

# Object of class D (hybrid)
ob3 = D()
ob3.show1()
ob3.show2()
ob3.show3()
ob3.show4()

