class Circle():
    def __init__(self):
        self.__radius=7

    @property
    def show(self):
        print(f"Radius is {self.__radius}")

    @show.setter
    def show(self,value):
        self.__radius=value

    @property
    def area(self):
        a=(3.14*(self.__radius**2))
        print(f"Area of circle is : {a}")

ob=Circle()
ob.show = 11
ob.area