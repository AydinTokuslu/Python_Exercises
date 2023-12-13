# Write a function called password_validator. The function
# asks the user to enter a password. A valid password should have
# at least one upper letter, one lower letter, and one
# number. It should not be less than 8 characters long. When
# the user enters a password, the function should check if the
# password is valid. If the password is valid, the function should
# return the valid password. If the password is not valid, the
# function should tell the users the errors in the password and
# prompt the user to enter another password. The code should
# only stop once the user enters a valid password. (use while loop).

def password_validator():
    errors = []
    while True:
        password = input("please enter your minimum 8 character password.\nPassword should have at least one upper letter, "
                     "one lower letter, and one number")
        if len(password) < 8:
            print("Your password should be 8 characters")
        elif password.isdigit():
            print("Your password should have at least one upper letter, one lower letter")
        elif password.islower():
            print("Your password should have at least one upper letter, one number")
        elif password.isupper():
            print("Your password should have at least one lower letter, one number")
        else:
            return f"Your password is : {password}"