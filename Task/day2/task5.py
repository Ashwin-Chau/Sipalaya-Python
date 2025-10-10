#To take sentence as input
sentence = input("Enter a sentence : ")

# Capitalize the first letter of each word in a sentence.
print(sentence.title())

# Replace spaces with underscores in a string.
print(sentence.replace(" ","_"))

'''
replace double space into single space :
input ="hello  world"
output="hello world"
'''

word="hello  world"
print(word.replace("  "," "))