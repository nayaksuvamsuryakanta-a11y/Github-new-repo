# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# Function to calculate sin(x) using series
def sin_series(x, n):
    total = 0
    for i in range(n):
        power = 2 * i + 1
        term = ((-1) ** i) * (x ** power) / factorial(power)
        total += term
    return total


# Function to calculate cos(x) using series
def cos_series(x, n):
    total = 0
    for i in range(n):
        power = 2 * i
        term = ((-1) ** i) * (x ** power) / factorial(power)
        total += term
    return total


# Main Program
x = float(input("Enter angle in radians: "))
n = int(input("Enter number of terms: "))

sin_x = sin_series(x, n)
cos_x = cos_series(x, n)

print("sin(x) =", sin_x)
print("cos(x) =", cos_x)

value = sin_x**2 + cos_x**2
print("sin^2(x) + cos^2(x) =", value)
