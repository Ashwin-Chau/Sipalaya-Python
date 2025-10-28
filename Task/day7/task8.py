'''
Task:
write a program to display all prime number within an interval
start=10
end=20
output=[11,13,17,19]
'''

output = []
for i in range(10,20):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            output.append(i)


print(output)


