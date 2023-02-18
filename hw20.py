"""

Given a single string. Find out how many times each word
apperas in the text, using dict.

"""

# initialize word string, words_dict - dictionary
word = ''
words_dict = {}

# promt user for an input
text = input("Enter text: ")

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

# print dict
for word in words_dict:
    print(f"{word}: {words_dict[word]}")
