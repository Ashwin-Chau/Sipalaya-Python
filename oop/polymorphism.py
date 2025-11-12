#polymorphism : poly means many morphism means form
#one thing behave in many way

# a="sujan"
# b="ram"
# print(len(a))
# print(len(b))


#types of polymorphism
#duck type
#method overloading(compile time)
#method overriding
#operator overloading


#duck type : Duck Typing means that Python cares about what an object can do, not what type it is. 
# “If it walks like a duck and quacks like a duck, it’s a duck.”
# So — instead of checking an object’s type (isinstance()), Python just tries to call the method or attribute.
# If the object supports it, it works! ✅
# If not, it fails. ❌


# class A():
#     def course(self):
#         print("i want to learn django")

# class B():
#     def course(self):
#         print("i want to learn data science")

# dipendra=A()
# prajwol=B()

# # dipendra.course()
# # prajwol.course()


# def show(a): #a=dipendra
#     a.course()

# show(dipendra)
# show(prajwol)




#method overloading(compile time polymorphism) : don't support on python
# class contain more than one method with same name but different parameter

# class A():
#     def show(self):
#         print("hello sipalaya")

#     def show(self,a,b):
#         print(a+b)

#     def show(self,a,b,c):
#         print(a+b+c)

# ob=A()
# ob.show()
# ob.show(2,3)
# ob.show(2,3,4)



# class A():
#     def show(self,a=0,b=0,c=0):
#         print(a+b+c)

# ob=A()
# ob.show(2,3)



#method overriding ---> class contain same method on both child class and parent class

# class A():
#     def show(self):
#         print("this is me")

# class B(A):
#     def show(self):
#         super().show()
#         print("this is you")
#         # super(): it is inbuilt function that is used to access attribute or method from parent
        

# ob=B()
# ob.show()



#operator overloading : with same operator is allowed to have different meaning according context

# print("2"+"2") #concatination
# print(2+2) #adding
# print([1,2,3]+[1,2,3]) #merge

#dunder dunction
# class A():
#     def __init__(self,x):
#         self.x=x

#     def __add__(self,other):
#         return self.x+other.x
    
#     def __sub__(self,other):
#         return self.x-other.x
    
#     def __eq__(self, other):
#         return self.x==other.x
    
#    # a/b a.__truediv__(b)
# ob=A(20)
# ob2=A(50)
# print(ob.x)
# print(ob + ob2)

# ob=A("20")
# ob2=A("70")
# print(ob + ob2)

# ob=A(7)
# ob2=A(4)
# print(ob - ob2)

# ob=A(7)
# ob2=A(7)
# print(ob == ob2)

# print(2 + 2)



#magic function :
# class A():
#     def __init__(self,name):
#         self.name=name

#     def __str__(self):
#         return "welcome "+self.name
    
#     def __call__(self):
#         print("this is debugging")

# ob=A("ram")
# print(ob)

# a=A("sujan")
# print(a)

# ob=A("ram")
# v=ob()




# class A():
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         print("B")
#         super().show()
# class C(A):
#     def show(self):
#         print("C")
#         super().show()
# class D(B,C):
#     def show(self):
#         print("D")
#         super().show()

# ob=D()
# ob.show()

# D ---> B --- > C ---> A



class A():
    def show(self):
        print("A")
        super().show()
class B():
    def show(self):
        print("B")
       
class C(A,B):
    def show(self):
        print("C")
        super().show()

ob=C()
ob.show()

# C ---> A -----> B 