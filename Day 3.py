1 power of 2
# Program to display powers of 2 up to 2^n
n = int(input("Enter a positive integer n: "))

# Loop through from 1 to n (inclusive)
for i in range(1, n+1):
    print(f"2^{i} = {2**i}")


2 display words
# Program to display a word based on user input
user_input = input("Enter either 'A', 'B', or 'C': ").upper()

if user_input == 'A':
    print("Apple")
elif user_input == 'B':
    print("Banana")
elif user_input == 'C':
    print("Coconut")
else:
    print("Invalid input. Please enter 'A', 'B', or 'C'.")



3 college status
# Program to display college status based on credits earned
credits = int(input("Enter the number of college credits earned: "))

if credits > 90:
    print("Senior Status")
elif credits > 60:
    print("Junior Status")
elif credits > 30:
    print("Sophomore Status")
else:
    print("Freshman Status")



4 sum of positive integers
# Program to sum positive integers excluding numbers greater than 100
total_sum = 0

while True:
    num = int(input("Enter a positive integer (or 0 to stop): "))
    if num == 0:
        break
    if num <= 100:
        total_sum += num

print("The sum of the entered integers (excluding numbers > 100) is:", total_sum)


5 counting integers
# Program to count positive and negative integers
positive_count = 0
negative_count = 0

while True:
    num = int(input("Enter an integer (or 0 to stop): "))
    if num == 0:
        break
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print(f"Number of positive values entered: {positive_count}")
print(f"Number of negative values entered: {negative_count}")

