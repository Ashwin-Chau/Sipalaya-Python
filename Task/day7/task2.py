'''
Task: Sum All Numbers in a List
input=[10, 20, 30, 40, 50]
Expected output : Sum of numbers: 150
'''

number = [10, 20, 30, 40, 50]
total = 0

for i in number:
    total += i
    
print(f"Sum of numbers: {total}")