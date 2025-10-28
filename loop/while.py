# while loop : run until condition is true

#syntax:
# while condition:
#     block of code


# a = 20

# while a<50:
#     print("a is less than 50")


# while True:
#     print("ashwin")

# a = 0   #initial condition

# while a<5:  #stop condition
#     # print("ashwin")
#     print("ashwin",a)

#     a+=1    #step

# import time

# start=time.time()
# for i in range(1000000):
#     pass
# end=time.time()
# print("for loop",end-start)


# start=time.time()
# i=0
# while i<1000000:
#     i+=1

# end=time.time()
# print("while loop",end-start)




secret="ashwin"

guess=""

while secret != guess:
    guess=input("enter your guess : ")

else:
    print("your guess is correct")