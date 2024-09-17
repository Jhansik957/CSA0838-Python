from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Get the first key from the difference between Counter(t) and Counter(s)
        return list((Counter(t) - Counter(s)).keys())[0]

# Example usage
solution = Solution()
s = "abcd"
t = "abcde"
print("The difference is:", solution.findTheDifference(s, t))  # Output: "e"
