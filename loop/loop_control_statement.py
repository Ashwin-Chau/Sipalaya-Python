#loop control statement : it is used to change the flow of execution, skip the iteration or stop the execution

#type of loop control statement
#pass statemnet
#break
#continue


# for i in range(10):
#     print(i)

#pass statement : pass in null statement that is used future code

# for i in range(10):
#     pass

# print("hello ashiwn")


#break : it is used to terminate the loop when encounter

# accounts = ["ram","ashwin","hari","syam"]

# for i in accounts:
#     if i == "ashwin":
#         print("your account is available")
#         break


# for i in range(10):
#     print(i)
#     if i == 5:
#         break



#continue : it is used to stop the current iteration and pass to another iteration

# for i in range(1,10):
#     if i % 3 == 0:
#         continue
#     print(i)


# names = ["sujan","dipendra","gita","ashiwn","sabnam"]

# for i in names:
#     if i.startswith("s"):
#         continue
#     print(i)



#else 


# a = [1,2,3,4,5,6]

# for i in a:
#     print(i)


# print("end")


# a = [1,2,3,4,5,6]

# for i in a:
#     print(i)

# else:
#     print("end")



# a = [1,2,3,4,5,6]
a = [1,2,3,4,0,5,6]

for i in a:
    if i == 0:
        print("zero is found !!!")
        break

else:
    print("zero is not found")