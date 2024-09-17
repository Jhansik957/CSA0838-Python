class Solution:
    def countSegments(self, s: str) -> int:
        # Split the string by spaces and count segments that are non-empty
        return len([segment for segment in s.split() if segment])

# Example usage
solution = Solution()
print(solution.countSegments("Hello, World! 123"))  # Output: 3
print(solution.countSegments("   "))  # Output: 0
print(solution.countSegments("abc 123 def456"))  # Output: 4
print(solution.countSegments("This is a test."))  # Output: 5
