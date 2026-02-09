numbers = [1, 2, 3, 4, 5, 6, 7]

for num in numbers:
    if num == 2:
        continue
    if num == 5:
        pass
    if num == 7:
        break
    print(num)
