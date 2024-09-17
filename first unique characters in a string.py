from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        return next((i for i, char in enumerate(s) if Counter(s)[char] == 1), -1)
solution = Solution()
s = "loveleetcode"
print("Index of first unique character:", solution.firstUniqChar(s))
