#operator ----> it is just a symbol which is used perform operation between operand

# a+b=50
# operand ---> a,b,50
# operator ---> +,=


#Arithmetic operator

# a=53
# b=7

# print(a+b) #addition
# print(a-b) #subtract
# print(a*b) #multiply
# print(a/b) #division
# print(a//b) #floor
# print(a**b) #exponential
# print(a%b) #modulus


#relative operator or comparision operator

# a=20
# b=30

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)


#assignment operator : =, +=, -=, *=, /=, //=, **=, %=
# a="ashwin"

# a=30
# # a=a+1
# a += 1
# print(a)



#logical operator : and, or, not

# a=20
# b=30

# print(a<b and a==b)  #Ture and False
# print(False and False)
# print(True and True)

# print(a<b or a==b)
# print(False or False)

# print(not a<b)




#membership operator (in, not in)

# a="my name is ashiwn"
# print("my" in a)
# a=["ashiwn",1,2,3,4]

# print(4 in a)
# print(4 not in a)





#identity operator (is, is not) #mutable have different memory address

# a=20
# b=20
# a=[1,2,3]
# b=[1,2,3]

# print(a is b)
# print(a is not b)

# print(id(20))
# print(id(a))
# print(id(b))

# print(a == b) #== checks value
# print(a is b) #is checks memory address




#bitwise operator (&, |, ~)
#it is individual of bit of integer

# a=12 #1100
# b=13 #1101

# print(a & b)
# print(a | b)
# print(~ a)


#8421 rule to find binary 
# & works
# 1100 ----> 12
# 1101 -----> 13
# -----
# 1100 ----> 12


# | works
# 1100
# 1101
# ------
# 1101  ----> 13



# ~ works (2's complement) 
# 0 0001100
# 1 1110011
# 1100
#   +1
# ------
# 1101

# -1101 ----> -13




#percedence

# ()
# exponential  ---> right to left
# *,/,//,%  -----> left to right
# +,- ----> left to right

# print((2**3)**2) # 2**3 ----> 8**2 ----> 64
# print(2**3**2) # 3**2 ------> 2**9 ----> 512
print(2*3**3//4)  # 2*27//4 ------> 54//4 ----> 13