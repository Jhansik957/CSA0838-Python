1 raised to power of 2
# Get input from the user
power = int(input("Enter an integer: "))

# Calculate 2 raised to the power
result = 2 ** power

# Display the result
print(f"2 raised to the power of {power} is {result}")


2 base and exponent
# Get base and exponent from the user
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Calculate base raised to the exponent
result = base ** exponent

# Display the result
print(f"{base} raised to the power of {exponent} is {result}")


3 binary to decimal
# Get four binary digits from the user
digit1 = input("Enter the leftmost binary digit: ")
digit2 = input("Enter the next binary digit: ")
digit3 = input("Enter the next binary digit: ")
digit4 = input("Enter the rightmost binary digit: ")

# Combine the digits to form a binary string
binary_string = digit1 + digit2 + digit3 + digit4

# Convert the binary string to decimal
decimal_value = int(binary_string, 2)

# Display the decimal value
print(f"The decimal value of the binary number {binary_string} is {decimal_value}")


4 division of integers
# Get two integer inputs from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform division and format the result to two decimal places
result = num1 / num2

# Display the result with exactly two decimal places
print(f"The result of {num1} divided by {num2} is {result:.2f}")


5 division by floating point inputs
# Get two floating-point inputs from the user
num1 = float(input("Enter the first floating-point number: "))
num2 = float(input("Enter the second floating-point number: "))

# Perform division and format the result to six decimal places
result = num1 / num2

# Display the result with exactly six decimal places
print(f"The result of {num1} divided by {num2} is {result:.6f}")

