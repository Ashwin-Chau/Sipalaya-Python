'''
Write a Python program to create a person class. Include attributes like name, country and date of birth.
 Implement a method to determine the person's age.
'''

class Person:
    def __init__(self,name,country,date_of_brith):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_brith

    def age(self):
        age = 2025-self.date_of_birth
        print(f"Your age is : {age}")

ob=Person("Ashwin","Nepal",2003)
ob.age()