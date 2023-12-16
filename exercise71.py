# Write a function called translate that takes the following
# words and translates them into pig Latin.
# a = 'i love python'
# Here are the rules:
# 1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the
# end. For example, ‘eat’ will become ‘eatyay’
# 2. If a word starts with anything other than a vowel, move
# the first letter to the end and add ‘ay’ to the end. For
# example, ‘day’ will become ‘ayday’.
# Your code should return:
# iyay ovelay ythonpay

def translate(str):
    vowel = ["a", "e", "i", "o", "u"]
    new_str = ""
    str = str.split(" ")
    for i in str:
        if i[0] in vowel:
            i += "yay"
            new_str+=i+" "
        else:
            i = i[1::]+i[0]
            print(i)
            i += "ay"
            new_str+=i+ " "
    print(new_str)


a = "i love python"
print(translate(a))