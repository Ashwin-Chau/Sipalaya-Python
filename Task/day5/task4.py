'''
Remove duplicate value from list 
input=["ram",1,2,3,3,4,4,4]
ouput=["ram",1,2,3,4]
'''

#set print in random order
# input=["ram",1,2,3,3,4,4,4]
# tuple = set(input)
# list = list(tuple)
# print(list)


input=["ram",1,2,3,3,4,4,4]

dict = dict.fromkeys(input)
list = list(dict.keys())
print(list)

