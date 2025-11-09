'''
Write a Python function that takes a list of integers as
input and returns a new list with the elements sorted in descending order,
 but with all odd numbers appearing before all even numbers.
'''

# a = [1,2,3,4,5]
# b = [5, 2, 9, 1, 6, 4, 7, 3, 8]
# def decending(list):
#     odd_list = []
#     even_list = []
#     list.sort(reverse=True)
#     for i in list:
#         if i % 2 == 0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)

#     return odd_list + even_list


# print(decending(a))
# print(decending(b))


b = [5, 2, 9, 1, 6, 4, 7, 3, 8]
def sort(lists):
    lists.sort(reverse=True)
    even_list = list(filter(lambda a:a%2==0, lists))
    odd_list = list(filter(lambda a:a%2!=0, lists))


    return odd_list + even_list

print(sort(b))