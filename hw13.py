"""

In the given string replace all instances of h
with H, except first and last h.


"""
string = input("String: ")

print(string[:string.find('h') + 1], string[string.find('h') + 1: string.rfind('h')].replace('h', 'H'), string[string.rfind('h'):], sep='')
