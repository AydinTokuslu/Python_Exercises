# Write a function called find_index that takes two arguments;
# a list of integers, and an integer. The function should return the
# indexes of the integer in the list. If the integer is not in the list,
# the function should convert all the numbers in the list into the
# given integer.
# For example, if the list is: [1, 2, 4, 6, 7, 7] and the integer is 7,
# your code should return [4, 5] as the indexes of 7 in the list. If
# the list is [1, 2, 4, 6, 7, 7] and the integer is 8, your code should
# return [8, 8, 8, 8, 8, 8] because 8 is not in the list.

def find_index(list1,num1):
    indexes = []
    if num1 in list1:
        for i in list1:
            if i == num1:
                indexes.append(list1.index(i))
        print(indexes)
    else:
        for i in range(len(list1)):
            indexes.append(num1)
        print(indexes)


list = [1, 2, 4, 6, 7, 7]
num = 7
find_index(list,num)