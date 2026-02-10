nums = [1, 2, 3, 4, 5, 6, 7]
size = 3

chunks = []

for i in range(0, len(nums), size):
    chunks.append(nums[i:i+size])

print(chunks)
