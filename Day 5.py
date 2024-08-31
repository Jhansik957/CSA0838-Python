1 anagrams
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for accurate comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Example usage
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False


2 finding anagrams
from collections import defaultdict

def find_anagrams(words):
    anagrams = defaultdict(list)
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    for group in anagrams.values():
        if len(group) > 1:
            print(group)

# Example usage
word_list = input("Enter words separated by spaces: ").split()
find_anagrams(word_list)


3 binary representation
n = int(input("Enter a positive integer: "))
binary_representation = bin(n)[2:]  # bin() returns a string prefixed with '0b'
print("Binary representation:", binary_representation)


4 word count
text = input("Enter text: ")
words = text.split()  # Splits the text by whitespace
word_count = len(words)
print("Number of words:", word_count)


5 star pattern
n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):
    print('*' * i)
