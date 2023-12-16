# Write a function called guess_a_number. The function
# should ask a user to guess a randomly generated number. If the
# user guesses a higher number, the code should tell them that the
# guess is too high, if the user guesses low, the code should tell
# them that their guess is too low. The user should get a maximum
# of three guesses. When the user guesses right, the code should
# declare them a winner. After three wrong guesses, the code
# should declare them a loser.

from random import randint

def guess_a_number():
    guess = 0
    random_num = randint(1,10)
    while guess <= 3:
        num = int(input("please enter a number : "))
        guess += 1
        if num > random_num:
            print("please enter a lower number")
        elif num < random_num:
            print("please enter a higher number")
        else:
            print("congratulations, you won")