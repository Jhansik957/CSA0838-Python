class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(char in it for char in s)
solution = Solution()
s = "abc"
t = "aebdc"
print("Is subsequence:", solution.isSubsequence(s, t))
