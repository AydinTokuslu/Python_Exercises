# Write a function called count that takes one argument a string,
# and returns a dictionary of how many times each element
# appears in the string. For example, ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.

def count(str):
    element = {}
    for i in str:
        if i not in element.keys():
            element[i] = 1
        else:
            element[i] += 1
    return element


s = "hello"
print(count(s))