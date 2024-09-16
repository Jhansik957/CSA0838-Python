import math
radius = float(input("Enter the radius of the circle: "))
print(f"Area: {math.pi * radius ** 2:.2f}")




binary_string = input("enter the binary string:")
decimal_value = int(binary_string,2)
print(decimal_value)




filename = 'name.txt'  # Replace with your file name

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f'The file has {len(lines)} lines.')
except FileNotFoundError:
    print(f'The file {filename} does not exist.')



list1 = ["apple", "banana", "cherry", "date", "elderberry"]
list2 = ["banana", "cherry", "fig", "grape"]
result = list(set(list1) - set(list2))
print(result)



def find_insert_position(nums, target):
    for i in range(len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)  
nums = [1, 3, 5, 6]
target = 5
print("Output:", find_insert_position(nums, target))
nums = [1, 3, 5, 6]
target = 2
print("Output:", find_insert_position(nums, target))



list1 = list(map(int, input("Enter integers for the first list: ").split()))
list2 = list(map(int, input("Enter integers for the second list: ").split()))
print("Same length:", len(list1) == len(list2))
print("Same sum:", sum(list1) == sum(list2))
print("Common values:", set(list1) & set(list2))



total_sum = 0
while True:
    number = int(input("Enter a positive integer (negative number to stop): "))
    if number < 0:
        break
    if number <= 100:
        total_sum += number
print("Total sum:", total_sum)


