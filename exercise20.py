# Write a function called equal_strings. The function takes two
# strings as arguments and compares them. If the strings are equal
# (if they have the same characters and have equal length), it
# should return True, if they are not, it should return False. For
# example, ‘love’ and ‘evol’ should return True.

def equal_strings(str1,str2):
    different_letter = ""
    global random_list
    random_list = []
    if len(str1) == len(str2):
        print("two words have the same lenght")
        for i in range(len(str1)):
            if str1[i] not in str2:
                different_letter += str1[i]
            elif str2[i] not in str1:
                different_letter += str2[i]
    else:
        print(f"two words have different lenght")
        return False

    if len(different_letter) == 0:
        print("two words have the same letters.")
        return True
    else:
        print(f"two words have the different letters = {different_letter}")
        return False

print(equal_strings("love","evol"))