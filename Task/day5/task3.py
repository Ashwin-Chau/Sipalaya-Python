'''
take three lists as input and returns a set of elements that are common to all three lists

Example input: [1,2,3,4], [2,3,4,5], [3,4,5,6] → Output: {3, 4}
'''

list1 = [1,2,3,4]
list2 = [2,3,4,5]
list3 = [3,4,5,6]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

common_numbers = set1.intersection(set2).intersection(set3)
print(common_numbers)

