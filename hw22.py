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
        if value in d_reversed:
            d_reversed[value].append(key)
        else:
            d_reversed[value] = [key]

# print result
print(d_reversed)