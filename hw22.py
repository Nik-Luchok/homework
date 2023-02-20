"""

Change key = value to value = key from a given dict

"""

# init the dict
d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'mutte']
}

# init new dict
d_reversed = {}

# iterate the touple, given back by d.items()
for key, value_list in d.items():
    for value in value_list:
        d_reversed[value] = key

# print result
print(d_reversed)