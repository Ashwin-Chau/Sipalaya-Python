'''
Accept age of 4 people and print youngest age
'''

age1 = int(input("Enter 1st person age : "))
age2 = int(input("Enter 2nd person age : "))
age3 = int(input("Enter 3rd person age : "))
age4 = int(input("Enter 4th person age : "))


# if (age1 < age2) and (age1 < age3) and (age1 < age4):
#     print("First person is youngest")

# elif (age2 < age3) and (age2 < age4):
#     print("Second person is youngest")

# elif (age3 < age4):
#     print("Third person is youngest")

# else:
#     print("Fourth person is youngest")


youngest = min(age1,age2,age3,age4)
print(f"Youngest person age is {youngest}")