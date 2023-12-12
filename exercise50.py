# Write a function called unique_numbers that takes a list of
# numbers as an argument. Your function is going to find all the
# unique numbers in the list. It will then sum up the unique
# numbers. You will calculate the difference between the sum of
# all the numbers in the original list and the sum of unique
# numbers in the list. If the difference is an even number, your
# function should return the original list. If the difference is an
# odd number, your function should return a list with unique
# numbers only. For example [1, 2, 4, 5, 6, 7, 8, 8] should
# return [1, 2, 4, 5, 6, 7, 8, 8].

def unique_numbers(x):
    unique_list = []
    not_unique_list = []
    sum_unique_numbers = 0
    sum_not_unique_numbers = 0
    sum_total_numbers = 0
    for i in x:
        sum_total_numbers += i
        if i not in unique_list:
            unique_list.append(i)
            sum_unique_numbers += i
        else:
            not_unique_list.append(i)
            sum_not_unique_numbers += i

    difference = sum_total_numbers - sum_unique_numbers - sum_not_unique_numbers
    if difference %2 == 0:
        print(x)
    else:
        print(not_unique_list)


list = [1, 2, 4, 5, 6, 7, 8, 8]
unique_numbers(list)

