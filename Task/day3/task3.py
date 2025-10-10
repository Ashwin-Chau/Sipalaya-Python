'''
Task:
Write a Python program that takes a list of numbers and give the second largest number in the list
input=[4,5,1,4,2,3,8,9,11,55,0,9]
output=11
'''

# list=[4,5,1,4,2,3,8,9,11,55,0,9]
# list.sort()
# print(list[-2])

# using reverse
list=[4,5,1,4,2,3,8,9,11,55,0,9]
list.sort(reverse=True)
print(list[1])