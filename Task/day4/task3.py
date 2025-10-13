'''
Task:
Python program that creates a dictionary representing a student's grades in different subjects
and then calculates the student's average grade
'''
grades = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "History": 88,
    "Computer": 92
}

average = sum(grades.values()) / len(grades)
print(f"Student's average grade is {average}")
