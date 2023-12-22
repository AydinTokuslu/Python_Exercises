# Write a function called analyse_string that returns the number of
# special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words,
# and, total characters (all letters and special characters minus
# whitespaces) in a string. Return everything in a dictionary format:

# {“special character”: “number”, “words”: “number”, “total
# characters”: “number”}

# Use the string below as an argument:

# “Python has a string format operator %. This functions
# analogously to printf format strings in C, e.g. "spam=%s
# eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".

def analyse_string(str):
    special_characters = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    special_char = ""
    total_char_count = 0
    for i in str:
        if i in special_characters:
            special_char += i

    words = str.split()
    num_words = len(words)

    for word in words:
        total_char_count += len(word)

    return f"special characters: {len(special_characters)},\nwords: {num_words},\ntotal characters: {total_char_count}"


str = "Python has a string format operator %. This functions analogously to printf format strings in C, e.g. 'spam=%s eggs=%d' % ('blah', 2) evaluates to 'spam=blah eggs=2'."

print(analyse_string(str))