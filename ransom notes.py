from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)
solution = Solution()
ransomNote = "aa"
magazine = "aab"
print("Can construct ransom note:", solution.canConstruct(ransomNote, magazine))  # Output: True
