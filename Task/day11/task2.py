'''
Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'My Name is Sujan' Expected Output : No. of Upper case characters : 3 No. of Lower case Characters : 10
'''

string = 'My Name is Sujan'

def upperlower(string):
    upper_count = 0
    lower_count = 0
    for i in string:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1

    print(f"No. of Upper case charcter : {upper_count} and No. of lower case Characters : {lower_count}")

upperlower(string)