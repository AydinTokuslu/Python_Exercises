
def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


num=int(input("please enter a number : "))