# Write a function called any_number that can receive any
# number of arguments (integers and floats) and return the
# average of those integers. If you pass 12, 90, 12, 34 as
# arguments your function should return 37.0 as average. If you
# pass 12, 90 your function should return 51.0 as average.

#def any_number(list):
#    average = 0
#    for i in list:
#        average += i
#    average = average/len(list)
#    return average

#list = [12, 90, 12, 34]
#print(any_number(list))

def any_number():
    average = 0
    sayi = int(input("how many numbers will you enter (to exit, press a) : "))
    for i in range(sayi):
        num = int(input(f"{i+1}. number : "))
        average += num
    average /= sayi
    print(f"All the {sayi} numbers average is : {average}")

any_number()






