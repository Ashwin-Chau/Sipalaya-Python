'''
Write a Python function that takes two lists of integers as input and 
# returns a new list containing only the numbers that are present in 
# both lists, but with each number appearing only once in the final list
'''

a = [1,2,3,4,12,10]
b = [5, 2, 9, 1, 6, 4, 7, 3, 8]

def repeat(list1,list2):
    new_list = []
    for i in set(list1):
        for j in set(list2):
            if i == j:
                new_list.append(i)
    
    return new_list

print(repeat(a,b))


