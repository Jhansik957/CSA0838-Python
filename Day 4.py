1 is power
def is_power(a, b):
    if a == b:  # Base case
        return True
    if a % b != 0:  # If not divisible
        return False
    return is_power(a // b, b)  # Recursive call

# Sample usage
print(is_power(8, 2))  # True, since 8 = 2^3
print(is_power(10, 2))  # False


2 finding gcd
def gcd(a, b):
    if b == 0:  # Base case
        return a
    return gcd(b, a % b)  # Recursive call

# Sample usage
print(gcd(48, 18))  # 6
print(gcd(100, 25))  # 25


3 frequency counting
def most_frequent(s):
    frequency = {}
    for letter in s:  # Count frequency
        frequency[letter] = frequency.get(letter, 0) + 1
    sorted_letters = sorted(frequency.items(), key=lambda x: x[1], reverse=True)  # Sort by frequency
    for letter, count in sorted_letters:
        print(letter, count)

# Sample usage
most_frequent("banana")


4 checking letters
def uses_only(word, letters):
    for letter in word:  # Check if all letters in the word are in the given letters string
        if letter not in letters:
            return False
    return True

# Sample usage
print(uses_only("apple", "aepl"))  # True
print(uses_only("banana", "abn"))  # False


5 triangular equality
def areTriangular(a, b, c):
    return a + b > c and a + c > b and b + c > a  

# Sample usage
print(areTriangular(3, 4, 5))  # True
print(areTriangular(1, 1, 2))  # False


