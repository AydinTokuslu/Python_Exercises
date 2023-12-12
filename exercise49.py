# s = 'Hi my name is Richard'
# Write a function called string_length that takes a string of
# words (words and spaces) as argument. This function should
# return the length of all the words in the string. Return the results
# in a form of a dictionary. The string above should return:
# {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}

def string_length(str):
    new_str = {}
    str = str.split(" ")
    for i in str:
        new_str[i] = len(i)
    return new_str

s = 'Hi my name is Richard'
print(string_length(s))