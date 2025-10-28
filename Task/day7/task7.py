'''
Task:
Python program to check the validity of password input by users
At least 8 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Contains at least one digit.
Contains at least one special character
note: Clearly indicate which specific requirements were not met
'''

special = ["!", "#", "@", "$", "%", "^", "&"]

while True:
    password = input("Enter a password: ")


    has_upper = has_lower = has_digit = has_special = False

    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special:
            has_special = True

    
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not has_upper:
        print("Password must contain at least one uppercase letter.")
    elif not has_lower:
        print("Password must contain at least one lowercase letter.")
    elif not has_digit:
        print("Password must contain at least one digit.")
    elif not has_special:
        print("Password must contain at least one special character (!, #, @, $, %, ^, &).")
    else:
        print("✅ You have a strong password!")
        break
