# Create a function called count_the_vowels. The function
# takes one argument, a string, and returns the number of vowels
# in the string. For example, ‘hello’ should return 2 vowels. If a
# vowel appears in a string more than once it should be counted
# as one. For example, ‘saas’ should return 1 vowel. Your code
# should count lowercase and uppercase vowels.

def count_the_vowels(str):
    vowels = ["a","e","i","o","u"]
    vowels_list = []
    for i in str:
        if i in vowels:
            if i not in vowels_list:
                vowels_list.append(i)
        else:
            continue
    return len(vowels_list)

#s = "hello"
s = "aslihan"
#s = "saas"
print(count_the_vowels(s))