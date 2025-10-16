#binary data types : it is used to handle raw binary data(sequence of byte) rather than text
#it is used for low level

#types of binary data types:
#bytes data types :
# it represent byte
# sequence of integer in the range 0-256
# immutable


#bit ----> 0,1
#byte ----> 8 bit 00000000(0) ----> 11111111(255)


# bit ----> 0,1
# byte ---> 8 bit 
# kilo byte ----> 1024 byte 
# mb ---> 1024 kb 
# gb ---> 1024 mb
# tb, pb, ex .....

# a=bytes([1,2,3,4])
# print(type(a))
# # a[0]=5 #don't support
# print(a[0])

# a=b"ashwin"
# print(type(a))


#bytearray : it is similar to byte but it is mutable

# a=bytearray([1,2,3,4])
# a[0]=5
# print(a)
# print(type(a))


# a=b"Ashiwn"
# b=memoryview(a)
# print(type(b))
# print(a[0])


#boolean data types
# a="ashwin" #True(1), False --> 0

# print(bool(a))


#None data Types
a=None
print(type(a))