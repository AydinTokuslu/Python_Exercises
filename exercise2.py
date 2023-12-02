# Write a function called longest_value that takes a dictionary
# as an argument and returns the first longest value of the
# dictionary. For example, the following dictionary should return
# – apple as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(dic):
    max = 1
    for i in dic:
        if len(dic[i]) > max :
            max = len(dic[i])
    return dic[i]

fruits = {'fruit': 'apple', 'color': 'greeen','shape': "circleee"}
print(longest_value(fruits))