'''
Write a Python program that takes a string and returns a dictionary where:
Keys are the unique characters in the string
Values are the counts of each character
input="aabbssssdka"
expected Output
{"a": 3, "b": 2, "s": 4, "d": 1, "k": 1}
'''

input = "aabbssssdka"

dict = {}

for i in input:
    if i in dict.keys():
        dict[i] = dict[i] + 1

    else:
        dict[i] = 1

print(dict)