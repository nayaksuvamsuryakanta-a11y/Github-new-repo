nums = [1,44,53,86,1111,88,1074]

largest = second = float('-inf')

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest:", second)
