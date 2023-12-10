# Write a function called capitalize. This function takes a string
# as an argument and capitalizes the first letter of each word. For
# example, ‘i like learning’ becomes ‘I Like Learning’.

def capitalize(str):
    str_new = ""
    for i in str.split(" "):
        str_new += i.capitalize()
        str_new += " "
    return str_new


str = "i like learning"
print(capitalize(str))