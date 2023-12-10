# Create three functions. The first called add_hash takes a string and
# adds a hash # between the words. The second function called
# add_underscore removes the hash (#) and replaces it with an
# underscore "_" The third function called remove_underscore,
# removes the underscore and replaces it with nothing. if you pass
# ‘Python’ as an argument for the three functions, and you call them at
# the same time like:
# print(remove_underscore(add_underscore(add_hash('Python'))))
# it should return ‘Python’.

def add_hash(str1):
    new_str1 = ""
    for i in str1:
        new_str1 += i
        new_str1 += "#"
    return new_str1

def add_underscore(str2):
    new_str2 = ""
    for i in str2:
        if i == "#":
            continue
        else:
            new_str2 += i
            new_str2 += "_"
    return new_str2

def remove_underscore(str3):
    new_str3 = ""
    for i in str3:
        if i == "_":
            continue
        else:
            new_str3 +=i
    return new_str3

str4 = "Python"
#print(add_hash(str4))
#print(add_underscore(add_hash(str4)))
print(remove_underscore(add_underscore(add_hash(str4))))

def add_hash1(a: str):
 return "#".join(a)
def add_underscore1(a: str):
 return str(a).replace("#", "_")
def remove_underscore1(a: str):
 return str(a).replace("_", "")
print(remove_underscore1(add_underscore1(add_hash1('Python'))))
