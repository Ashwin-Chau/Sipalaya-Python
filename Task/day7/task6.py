'''
Write a Python program that takes a list of elements and returns a new list containing only the elements that are palindromes 
(strings or numbers that read the same backward as forward)..
input=['apple','racecar',"carac","mam","orange",121,331]
output=['racecar','carac','mam',121]
'''

list = ['apple','racecar',"carac","mam","orange",121,331]

output = []

for i in list:
    if str(i)==str(i)[::-1]:
        output.append(i)

print(output)