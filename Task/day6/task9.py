'''
Write a Python program to check if a given key already exists in a dictionary
'''

my_dict = {
    "name":"ashwin",
    "age":22,
    "address":"chitwan"
}


key = input("Enter a key to search : ")

if key in my_dict.keys():
    print("Key already exist")

else:
    print("Key does not exist")