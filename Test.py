text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
my_list = []

n = 1

for el in text:
    for l in el:
        if len(l) <= n:
            my_list.append(l)


print(my_list)