# Create a function called average_calories that calculates the
# average calories intake of a user. The function should ask the user
# to input their calories intake for any number of days and once they
# hit ‘done’ it should calculate and return the average intake.

def average_calories():
    calories = []
    while True:
        calori = input("please enter the calorie, or enter 'done' to exit : ")
        if calori == "done":
            break
        else:
            calories.append(int(calori))
    return f"Average intake is {sum(calories)/len(calories)}"

print(average_calories())

