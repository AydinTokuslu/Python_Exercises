# Write a function called user_name, that creates a username
# for the user. The function should ask a user to input their name.
# The function should then reverse the name and attach a
# randomly issued number between 0 – 9 at the end of the name.
# The function should return the username.

import random
from random import *

def user_name():
    name = input("please enter a username:  ")
    name_reverse = name[::-1]
    random_num = randint(0,9)
    print(f"name reverse : {name_reverse}{random_num}")

user_name()
