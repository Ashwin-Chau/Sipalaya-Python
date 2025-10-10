


words={
    "mother":"आमा",
    "father":"बुबा",
    "love":"माया"
}

user=input("Enter your word to translate in nepali : ")
v=words.get(user,"word is not found")
# v=words[user]
print(v)