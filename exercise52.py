# Write a function called index_position. This function takes a
# string as a parameter and returns the positions or indexes of all
# lower letters in the string. For example, ‘LovE’ should return
# [1,2].


def index_position(str):
    index_num = []
    for i in str:
        if i.islower():
            index_num.append(str.index(i))
    return index_num

x = "LovE"
print(index_position(x))