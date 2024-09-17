from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))  # Remove duplicates
        unique_nums.sort(reverse=True)  # Sort in descending order
        if len(unique_nums) >= 3:
            return unique_nums[2]  # Return the third maximum number
        else:
            return unique_nums[0]  # If there are fewer than 3 distinct numbers, return the maximum

# Example usage
solution = Solution()
print(solution.thirdMax([3, 2, 1]))  
print(solution.thirdMax([1, 2]))     
print(solution.thirdMax([2, 2, 3, 1]))
