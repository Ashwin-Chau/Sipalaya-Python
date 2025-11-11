class A():
    def show(self):
        print("I am class A")

class B(A):
    def show(self):
        print("I am class B")
        super().show()

class C(A):
    def show(self):
        print("I am class C")
        super().show()

class D(B, C):
    def show(self):
        print("I am class D")
        super().show()

ob = D()
ob.show()