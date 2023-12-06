# Create a function called biggest_odd that takes a string of
# numbers and returns the biggest odd number in the list. For
# example, if you pass ‘23569’ as an argument, your function
# should return 9. Use list comprehension.

def biggest_odd(str):
    max_num = 0
    list_nums = []
    list_nums_int = []
    for i in range(len(str)):
        list_nums.append(str[i])
    print(list_nums)

    for i in range(len(list_nums)):
        list_nums_int.append(int(list_nums[i]))
    #print(max(list_nums_int))
    for i in range(len(list_nums_int)):
        if list_nums_int[i] > max_num:
            max_num = list_nums_int[i]
    print(max_num)




str = "23569"
biggest_odd(str)