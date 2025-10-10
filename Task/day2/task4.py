'''
Count Vowels in a Sentence
Description:
Write a program that:

Takes a sentence as input

Counts and displays the number of vowels (a, e, i, o, u, case-insensitive)
'''

#To take sentence as input
sentence = input("Enter a sentence : ")

#change to upper(case-insensitive)
sentence_upper = sentence.upper()

a_count = sentence_upper.count("A")
e_count = sentence_upper.count("E")
i_count = sentence_upper.count("I")
o_count = sentence_upper.count("O")
u_count = sentence_upper.count("U")


print("Number of 'a':", a_count)
print("Number of 'e':", e_count)
print("Number of 'i':", i_count)
print("Number of 'o':", o_count)
print("Number of 'u':", u_count)
