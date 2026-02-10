nums = [10, 5, 20, 8]

largest = nums[0]
smallest = nums[0]

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Max",largest)
print("Min",smallest)
