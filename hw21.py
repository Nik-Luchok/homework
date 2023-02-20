"""

Given multiple strings. Find out how many times
appears the most used word in the whole text, using dict.
If there are a few, print the latest (that appears in the text).

"""

# initialize word string, words_dict - dictionary
word = ''
words_dict = {}

# promt user for an input
text1 = input("Enter text: ")
text2 = input("Enter text: ")
text3 = input("Enter text: ")

# concatenate string into one text, add whitespace between
text = ' '.join([text1, text2, text3])

# iterate thru text to find words
for ch in text:
    # check a character wether it's alphabetical
    # or apostrof, but not at the start of the word
    if ch.isalpha() or (ch == "'" and len(word) != 0):
        # append the char to a word
        word += ch

    # if the word endet, and we encountered non alpha symbol
    elif len(word) != 0:
        # if the word present in dict
        if word in words_dict:
            # add + 1 to the counter
            words_dict[word] += 1

            # delete the word for the next one
            word = ''

        # new word, add to the dict
        else:
            words_dict[word] = 1

            # delete the word for the next one
            word = ''

# if text endet on word, without a punctuation symbol
if len(word):
    if word in words_dict:
        # add + 1 to the counter
        words_dict[word] += 1

    # new word, add to the dict
    else:
        words_dict[word] = 1

# find out how many times were used the most used words
words_max = max(words_dict.values())

# iterate the dict in reversed order, print the last most used word
print("Last most used word is:")
for word in reversed(words_dict):
    if words_dict[word] == words_max:
        print(word, end=" ")
        break
print()
