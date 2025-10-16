# type conversion : convert one data type to another data types

# type implicit (data conversion) : python interpreter automatically one data type to another

# a=23
# b=3.3
# c=a+b
# print(c)
# print(type(c))

# a=2
# a="2"
# a=True #1
# b=3
# c=a+b
# print(c)



# type explicit (type casting) : python developer convert one data type to another

# a=5
# b=2
# c=a/b
# c=int(c)
# print(c)

# a=12
# b=float(a)
# b=complex(a)
# b=str(a)
# print(b)


# a="12"
# a="ashwin"
# b=int(a)
# b=list(a)
# print(b)


# a=[1,2,3,4,5]
# b=tuple(a)
# b=set(a)
# b=str(a) # "[1,2,3,4,5]"
# print(b[0])
# print(type(b))


a={
    "name":"ashiwn",
    "age":77
}

b=list(a.items())
print(b)