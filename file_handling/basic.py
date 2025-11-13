'''
file handling : 

file : collection of data and information to store data permanent
type of file :
text file ---> used to store in form character : .py,.txt,csv,.html
binary file ---> used to store in form byte : image,video

file handling : python perform some function such as : create,read,write,append,delete
                for small project


process of file handling :
--->file open
--->perform some operation
--->close file

syntax :

f_object = open("file_path","mode")

mode: purpose of opening that file
x  ---> create
r  ---> read
w  ---> write
a  ---> append
r+ ---> read and write
w+ ---> write and read
a+ ---> write and read
'''

# a=input("Enter your name ")
# print(a)



# a=input("Enter your name ")
# f=open("msg.txt",'w')
# f.write(a)
# print(a)


# to create a file
# f=open("msg.txt",'x')


# to read a file 
# f=open("msg.txt",'r')
# f=open("msg.txt",) 
# f=open("msg.txt",mode='r') #use any of three

# print(f.read(10))
# print(f.readline())
# print(f.readlines())
# print(f.read())




# to write in file 
# f=open("msg.txt",'w') #it override the data
# f.write("okey sipalaya")
# f.write("\ni want to learn django")




# to append in file / to add something in existing file
# f=open("msg.txt",'a')
# f.write("okey sipalaya")



#to read and write
# f=open("msg.txt",'r+')
# print(f.read(10))
# f.write("okey sipalaya")




#to write and read
# f=open("msg.txt",'w+') # it overide the data
# print(f.read(10))
# f.write("okay sipalaya")




#to write and read but don't override the data
# f=open("msg.txt",'a+') 
# print(f.read(10))
# f.write("okay sipalaya")




# data loss problem
# f=open("msg.txt",'r')
# print(f.read(10))


# print("some imp code is here")





#
# f=open("msg.txt",'r')
# print(f.read(10))
# f.close()
# print(f.closed)

# print("some imp code is here")




# try:
#     f=open("msg.txt",'w')
#     print(f.read(10))
# finally:
#     f.close()
# print(f.closed)





# with statement : automatically closed the file

# with open("msg.txt",'r') as f:
#     print(f.read(10))

# print(f.closed)




#tell & seek  
#tell :- to find the position of cursor
#seek :- to set the cursor position

# f=open("msg.txt",'r')
# print(f.tell())
# print(f.read(10))
# print(f.tell())
# print(f.read(20))
# print(f.tell())



# f=open("msg.txt",'r')
# print(f.read(10))
# print(f.tell())
# f.seek(0)
# print(f.tell())
# print(f.read(20))




# import os
# os.remove("msg.txt")