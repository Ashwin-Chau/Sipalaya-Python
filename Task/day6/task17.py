'''
Write a program to print “Yes ” if input number is multiple by 3 else print “No”
'''

num = int(input("Enter a number : "))

if num % 3 == 0:
    print(f"{num} is Multiple of 3")

else:
    print("No")