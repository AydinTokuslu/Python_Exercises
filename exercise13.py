# You are given a list of names, and you are asked to write a code
# that returns all the names that start with ‘S’. Your code should
# return a dictionary of all the names that start with S and how
# many times they appear in the dictionary. Here is a list below:
# names = ["Joseph","Nathan", "Sasha", "Kelly",
#  "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
# Your code should return: {"Sasha": 1, "Sera": 2}


names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

s_list = []
for i in names:
    if i.startswith("S"):
        s_list.append(i)
print(s_list)
new_result = {m:s_list.count(m) for m in s_list}
print(new_result)