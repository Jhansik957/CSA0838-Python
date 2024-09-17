from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use a Counter to count occurrences of elements in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Find the intersection by taking the minimum count for each element
        result = []
        for num in count1:
            if num in count2:
                # Append the element as many times as it appears in both arrays
                result.extend([num] * min(count1[num], count2[num]))
        
        return result
