# Write a function called count_dots. This function takes a
# string separated by dots as a parameter and counts how many
# dots are in the string. For example, ‘h.e.l.p.’ should return 4
# dots, and ‘he.lp.’ should return 2 dots.

def count_dots(str):
    dots_number = 0
    str_a = str.split(".")
    print(str_a)
    for i in range(len(str_a)-1):
         dots_number += 1
    return f"number of dots = {dots_number}"

#str = "h.e.l.p."
str = "he.lp."
print(count_dots(str))