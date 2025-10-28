'''
Write a Python program to generate and print the first n numbers in the Fibonacci sequence,
 where each number is the sum of the two preceding ones, starting from 0 and 1.
0,1,0+1=1,1+1=2,2+1=3,3+2=5,5+3=8,8+5=13
'''


n = int(input("Enter how many Fibonacci numbers to print: "))

# Starting values
a, b = 0, 1

print("Fibonacci sequence:")

for i in range(n):
    print(a)
    a, b = b, a + b
