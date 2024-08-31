1 chop function
def chop(lst):
    if len(lst) > 2:
        del lst[0]  
        del lst[-1]  

# Example usage
lst = [1, 2, 3, 4, 5]
chop(lst)
print(lst)  


2 cunsum function
def cumsum(numbers):
    result = []
    total = 0
    for number in numbers:
        total += number
        result.append(total)
    return result

# Example usage
numbers = [1, 2, 3, 4]
print(cumsum(numbers))  


3 duplicate values
def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

# Example usage
lst = [1, 2, 3, 4, 1]
print(has_duplicates(lst))  


4 sorting
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Example usage
lst = [1, 2, 2, 3]
print(is_sorted(lst))  # Output: True


5 nested sum
def nested_sum(lst_of_lists):
    total = 0
    for inner_list in lst_of_lists:
        for number in inner_list:
            total += number
    return total

# Example usage
lst_of_lists = [[1, 2], [3, 4], [5]]
print(nested_sum(lst_of_lists))  # Output: 15


