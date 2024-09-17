class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        num &= 0xFFFFFFFF
        hex_str = hex(num)[2:]
        return hex_str
solution = Solution()
number = 26
print("Hexadecimal representation:", solution.toHex(number))  
number = -1
