"""

Find all indexes of a word/char that user inputet, in another string

"""

# user input
string = input("Provide string: ")
sub_string = input("Provide substring to search: ")

# search & print
index = string.find(sub_string)
print("Indexes: ", end="")
while index != -1:
    print(index, end=" ")
    index = string.find(sub_string, index + 1)
