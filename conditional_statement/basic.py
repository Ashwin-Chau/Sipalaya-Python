#conditional statement : Making decision based on value of variable hold or result
'''
#if statement:
syntax :
if condition(True/Fasle):
    #block of code


#if else statement

if comdition:
    block of code

else:
    block of code
'''

# price=10

# if price>20:
#     print("i can go to coffee shop")

# print("welcome")

# age=int(input("Enter your age : "))
# if age>=18:
#     print("You are eligible to vote")

# else:
#     print("You are not eligible to vote")





# if statement in single line

# a=10
# if a > 15:print("a is greater than 15")




#shorthand if-else statement (Ternary operator)

# a=10

# if a>15:
#     print("a is greater than 15")

# else:
#     print("a is less than 15")


# print("a is greater than 15") if a > 15 else print("a is less than 15")




# elif statement
'''
syntax :
if condition:
    block of code
elif condition:
    block of code
elif condition:
    block of code
else:
    block of code
'''

# print("bus ticket system")

# age=int(input("Enter your age : "))

# if age <= 12:
#     print("you are free to travel")

# elif age > 12 and age < 18:
#     print("you have to pay Rs. 20")

# elif age >=18 and age < 40:
#     print("You have to pay Rs. 100")

# else:
#     print("You have to pay Rs. 50")



# nested if statement

print("bus ticket system")

age=int(input("Enter your age : "))

if age <= 12:
    print("you are free to travel")

elif age > 12 and age < 18:
    print("you have to pay Rs. 20")

elif age >=18 and age < 40:
    if age == 30:
        print("You don't have to pay")

    else:
        print("You have to pay Rs. 100")

else:
    print("You have to pay Rs. 50")