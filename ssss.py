# Initial list
fruits = ["apple", "banana", "cherry"]

# 1. Manipulation
fruits.append("orange")         # Add to end
fruits.insert(1, "mango")       # Insert at specific index
fruits[0] = "strawberry"        # Update element

# 2. Removal
fruits.remove("banana")         # Remove first occurrence of value
popped = fruits.pop(0)          # Remove by index and return value

# 3. Slicing and Length
numbers = [10, 20, 30, 40, 50]
subset = numbers[1:4]           # Slicing from index 1 to 3
size = len(numbers)             # Get total number of items

print(f"Final List: {fruits}")
print(f"Slicing Result: {subset}")
