nums = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
