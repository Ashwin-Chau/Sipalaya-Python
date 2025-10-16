'''
Write a program to return the grade of a person according to the marks they received.  
Example:
input: Enter your marks: 90
Output : Distinction
'''

marks = float(input("Enter your marks : "))

if marks >= 90:
    print("Dictinction")

elif marks >= 80:
    print("First Division")

elif marks >= 70:
    print("Second Division")

elif marks >= 60:
    print("Third Division")

elif marks >= 50:
    print("Fourth Division")

elif marks >= 40:
    print("Fifth Division")

else:
    print("Fail")