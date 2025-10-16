# check given number is palindrome or not

# word = input("Enter a word : ")
word = 121
str_word = str(word)
reverse_word = str_word[::-1]

if str_word == reverse_word:
    print("It is palindrom")

else:
    print("It is not palindrome")