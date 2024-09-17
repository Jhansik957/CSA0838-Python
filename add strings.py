from typing import List

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        for i in range(max_len - 1, -1, -1):
            digit1 = int(num1[i])
            digit2 = int(num2[i])
            total = digit1 + digit2 + carry
            carry = total // 10
            result = str(total % 10) + result
        if carry:
            result = str(carry) + result

        return result

# Example usage
solution = Solution()
print(solution.addStrings("123", "456")) 
print(solution.addStrings("11", "123"))   
print(solution.addStrings("456", "77"))
