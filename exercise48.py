# Write a function called sort_words that takes a string of words
# as an argument, removes the whitespaces, and returns a list of
# letters sorted in alphabetical order. Letters will be separated by
# commas. All letters should appear once in the list. This means
# that you sort and remove duplicates. For example ‘love life’
# should return as ['e,f,i,l,o,v']

def sort_words(str):
    new_str = []
    for i in str:
        if i != " ":
            if i not in new_str:
                new_str.append(i)
    return sorted(new_str)

s = "love life"
print(sort_words(s))