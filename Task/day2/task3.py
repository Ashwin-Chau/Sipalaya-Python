'''
Write a Python program that:

Contains a predefined paragraph string

Takes a word as user input

Counts how many times that word appears in the paragraph (case-insensitive)

Outputs the count

paragraph = "The quick brown fox jumps over the lazy dog. The dog was not that lazy, really."
Enter a word to count: the
Word 'the' appears 3 times
'''

paragraph = "The quick brown fox jumps over the lazy dog. The dog was not that lazy, really."

# user input 
word = input("Enter a word to count: ")

#change paragraph to lower(case-insensitive)
paragraph_lower = paragraph.lower()
word_lower = word.lower()

# count how many times the word appears
count = paragraph_lower.count(word_lower)

print("Word '"+word_lower+"' appears" ,count, "times")

