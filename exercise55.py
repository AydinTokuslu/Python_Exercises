# Write a function called repeated_name that finds the most
# repeated name in the following list.
# name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]

def repeated_name(list):
    repeat_list = {}
    for i in list:
        if i not in repeat_list:
            repeat_list[i]=1
        else:
            repeat_list[i]+=1
    print(repeat_list)
    return f"most repeated name is : {max(repeat_list)} and repeat number is : {max(repeat_list.values())}"

name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeated_name(name))
