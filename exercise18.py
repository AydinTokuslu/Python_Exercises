# Write a function called hide_password that takes no
# parameters. The function takes an input (a password) from a
# user and returns a hidden password. For example, if the user
# enters ‘hello’ as a password the function should return ‘****’ as
# a password and tell the user that the password is 4 characters
# long.

def hide_password():
    password = input("please enter your password: ")
    if len(password) > 0 :
        new_password = len(password) * "*"
    print(f"Your password is {len(new_password)} characters long\nYour password is {new_password}")

hide_password()