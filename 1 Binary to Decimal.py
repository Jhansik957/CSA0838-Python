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
