# Create a simple calculator. The calculator should be able to perform
# basic math operations, add, subtract, divide and multiply. The
# calculator should take input from users. The calculator should be
# able to handle ZeroDivisionError, NameError, and ValueError.

def calculator():
    try:
        num1 = int(input("please enter a number : "))
        opt = input("please select an operator (+ - / *): ")
        num2 = int(input("please enter another number for calculation : "))
        if opt not in ['+', '-', '/', '*'] or len(opt)>1:
            print("please enter a correct operator (+ - / *) ")
    except ValueError:
        print("please enter a valid number ")
    except ZeroDivisionError:
        print("You cannot divide a number by zero.Try again ")
    else:
        if opt == "+":
            return f"answer is {num1+num2}"
        elif opt == "_":
            return f"answer is {num1-num2}"
        elif opt == "/":
            return f"answer is {num1/num2}"
        elif opt == "*":
            return f"answer is {num1*num2}"
    return "Try again"

print(calculator())
