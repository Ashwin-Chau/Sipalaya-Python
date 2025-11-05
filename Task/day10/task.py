def sum(n):
    if n == 0:
        return 0
    return n%10 + sum(n//10)

print(f"given number sum is {sum(1234)}")