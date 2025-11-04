'''
Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
'''


# def prime():
#     num = 7
#     count = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             count += 1

#     if count == 2:
#         print(f"{num} is prime number")
#     else:
#         print(f"{num} is not prime number")

# prime()





def prime_composite(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(f"{num} is prime number")
    else:
        print(f"{num} is composite number")


prime_composite(5)
prime_composite(6)
prime_composite(9)
prime_composite(7)
prime_composite(11)