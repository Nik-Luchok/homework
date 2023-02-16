"""

How many words in a sentence? 

"""

# take inut from user
sentence = input("Sentence: ")

# count spaces, add 1, we'll get the number of words
words = sentence.count(" ") + 1

print(words)