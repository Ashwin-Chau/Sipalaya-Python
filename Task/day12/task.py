class Circle:
    def __init__(self,radius):
        assert radius<0, f"{radius} cannot be in negative"
        self.radius = radius 

    def areaperimeter(self):
        if self.radius < 0:
            print("Cannot have a -ve value")
        else:
            area = self.radius**2*3.14
            perimeter = self.radius*2*3.14
            print(f"Area of circle of radius {self.radius} is {area} and perimeter is {perimeter}")


rad=Circle(-12)
rad.radius=45
rad.areaperimeter()
    