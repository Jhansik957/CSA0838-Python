class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define vowels set, including both lower and upper case vowels
        vowels = set("aeiouAEIOU")
        
        # List to store vowels in the string
        vowel_list = [char for char in s if char in vowels]
        
        # Reverse the list of vowels
        vowel_list.reverse()
        
        # Create a list of characters from the string
        s_list = list(s)
        
        # Initialize index for reversed vowels
        vowel_index = 0
        
        # Traverse through the string and replace vowels with reversed vowels
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = vowel_list[vowel_index]
                vowel_index += 1
        
        # Join the list back to form the final string
        return ''.join(s_list)

# Example usage:
sol = Solution()
s = "IceCreAm"
output = sol.reverseVowels(s)
print(output)


s = "leetcode"
output = sol.reverseVowels(s)
print(output)
