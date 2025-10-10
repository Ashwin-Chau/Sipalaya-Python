'''
Remove all vowel letter from strings which takes from user
input="my NAME Is sujan"
output="my nM s sjn"
'''

#to take string from users
string = input("Enter a string : ")

print(string.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','').replace('A','').replace('E','')
.replace('I','').replace('O','').replace('U',''))
