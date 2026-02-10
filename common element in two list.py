a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for x in a:
    if x in b and x not in common:
        common.append(x)

print(common)
