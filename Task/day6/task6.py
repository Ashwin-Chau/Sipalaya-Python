'''
Write a Python program that determines whether a given number falls within the range of 1 to 100 (inclusive).
 The program should output "In range" if the number is within this range and "Out of range" otherwise
'''

number = int(input("Enter a number : "))

if number >= 1 and number <= 100:
    print("In range")

else:
    print("Out of range")