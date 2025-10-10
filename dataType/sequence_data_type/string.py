#string : sequence of character enclosed in either single quote , double or triple

# a='ashwin said, "i wnat to learn django"'
# a="what's up"
# a='''my name is ashwin 
#     and i m from chitwan'''
# print(type(a))
# print(a)

# a="aswhin #"
# print(len(a))

#index : the way of accessing element by their position
#synatx : variable_name[position]

# a="ashwin"
# print(a[0])

#slicing : the way of accesing part of element
#syntax : variable_name[start:end:step]

# a="my name is ashwin" #name
# print(a[3:7:1])
# print(a[3:10:2]) #nm s
# print(a[6:2:-1]) #eman

# print(a[3:])
# print(a[:4])
# print(a[::])
# print(a[::-1])


#string method
# a="my NAME is ashwin"
# print(len(a))

# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.capitalize())
# print(a.title())
# print(a.casefold())


# a="welcome my name is ashiwn"

# # print(a.center(70,'-'))
# print(a.count("a"))

# value=''''''

# user = input

# a='my name is ashwin'
# print(a.replace("ashwin","ash"))
# print(a.startswith("my"))
# print(a.endswith("in"))
# print(a.isalnum())
# print(a.isascii())


#split
# a="my name is ashiwn"
# print(a.split())
# print(a.split("a"))

# a="ashwin123@gmail.com"
# print(a.split("@")[0])


#strip
# a="!!!welcome!!!"
# print(a.strip())
# print(a.strip("!"))
# print(a.rstrip("!"))
# print(a.lstrip("!"))

# a="www.hello.com"
# print(a.lstrip("www.").rstrip(".com"))
# print(a.removeprefix("www.").removesuffix(".com"))