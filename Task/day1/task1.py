'''
Task: Create Your Own Mad Libs Game
The program should generate a fun and unique story based on the user's inputs.
User input :
At least one noun
At least one verb
At least one adjective
At least one adverb

input:
Once upon a time, there was a very [adjective] [noun]. 
It loved to [verb] [adverb] every day in [place].

expected output:
Once upon a time, there was a very happy dog.
 It loved to jump gracefully every day in the garden
 
'''

#To take input from user
noun = input("Enter a noun : ")
verb = input("Enter a verb : ")
adjective = input("Enter an adjective : ")
adverb = input("Enter an adverb : ")
place = input("Enter a place : ")

# Output
print("Once upon a time, there was a very" ,adjective ,noun,".")
print("It loved to" ,verb ,adverb, "every day in" ,place,".")