# Create a function called words_with_vowels, this function
# takes a string of words and returns a list of only words that
# have vowels in them. For example, ‘You have no rhythm’ should
# return [‘You’,’have’, ‘no’].

def words_with_vowels(str):
    vowels = ["a", "e", "i", "o", "u"]
    str = str.split()
    new_list = []
    for i in str:
        for j in vowels:
            if j in i:
                if i not in new_list:
                    new_list.append(i)
    print(new_list)




str = "You have no rhythm"
words_with_vowels(str)