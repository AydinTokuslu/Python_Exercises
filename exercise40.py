# Write a function called even_or_average that ask a user to
# input five numbers. Once the user is done, the code should
# return the largest even number in the inputted numbers. If
# there is no even number in the list, the code should return the
# average of all the five numbers.

num_list = []
for i in range(5):
    num = int(input(f"please enter {i+1} numbers: "))
    num_list.append(num)

def even_or_average(num_list):
    sum = 0
    even_num = []
    for i in num_list:
        if i % 2 == 0 :
            even_num.append(i)
        else:
            sum += i
    if len(even_num) > 0:
        print(f"The max even number from the entered is : {max(even_num)} ")
    else:
        print(f"the average of the entered numbers is : {sum//len(num_list)}")

even_or_average(num_list)