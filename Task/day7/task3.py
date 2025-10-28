'''
Write a Python program that accepts a string and counts the number of upper and lower case letters. 
Sample String : 'My Name is Sujan' 
Expected Output : No. of Upper case characters : 3 No. of Lower case Characters : 10
'''

sentence = 'My Name is Sujan.'

upper = 0
lower = 0

for i in sentence:
    if i.islower():
        lower += 1

    # else:
    elif i.isupper():
        upper += 1

print(f"No. of Upper case characters : {upper} and No. of lower case Character : {lower}")
