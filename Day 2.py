1 division
# Predefined values (can be changed to user input in a real scenario)
num1 = 12.3456
num2 = 78.9012

# Perform division and display result in scientific notation with 6 decimal places
result = num1 / num2
print(f"The result of division is: {result:.6e}")


2 unicode value
# Predefined value (can be changed to user input)
letter = 'A'

# Convert to Unicode and display
unicode_value = ord(letter)
print(f"The Unicode encoding of {letter} is: {unicode_value}")


3 area
import math

# Predefined radius (can be changed to user input)
radius = 5

# Calculate the area
area = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is: {area:.2f}")


4 payment table
import sys

# Predefined values (can be changed to command-line arguments)
years = 30
principal = 300000
annual_interest_rate = 3.5

# Calculate monthly interest rate and number of payments
monthly_interest_rate = annual_interest_rate / 100 / 12
number_of_payments = years * 12

# Calculate the monthly payment using the formula for a fixed-rate mortgage
monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)

print(f"Monthly Payment: ${monthly_payment:.2f}")

# Display the payment table
remaining_principal = principal
for month in range(1, number_of_payments + 1):
    interest_paid = remaining_principal * monthly_interest_rate
    principal_paid = monthly_payment - interest_paid
    remaining_principal -= principal_paid
    print(f"Month {month}: Payment = ${monthly_payment:.2f}, Interest Paid = ${interest_paid:.2f}, Principal Paid = ${principal_paid:.2f}, Remaining Principal = ${remaining_principal:.2f}")



volume
import math

# Predefined radius
radius = 5

# Calculate the volume of the sphere
volume = (4/3) * math.pi * radius ** 3
print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")


