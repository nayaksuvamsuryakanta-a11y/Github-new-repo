# 1. Initialize a list
fruits = ["apple", "banana", "cherry"]

# 2. Add elements
fruits.append("orange")      # Adds to the end
fruits.insert(1, "mango")    # Adds at index 1

# 3. Access and Modify
print(f"Second item: {fruits[1]}")
fruits[0] = "strawberry"     # Change "apple" to "strawberry"

# 4. Remove elements
fruits.remove("cherry")      # Removes by value
popped_item = fruits.pop()   # Removes and returns the last item

# 5. List Slicing
numbers = [0, 1, 2, 3, 4, 5]
print(f"Middle slice: {numbers[1:4]}") # Elements from index 1 to 3

# 6. List Comprehension (Advanced but common)
squares = [x**2 for x in range(5)] # Creates [0, 1, 4, 9, 16]

# Final Output
print("Final Fruit List:", fruits)
print("Squares List:", squares)
