numbers = list(map(int, input("Enter numbers: ").split()))

for num in numbers:
    if num < 0:
        break
    print(num)
