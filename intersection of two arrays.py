from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets to remove duplicates and find the intersection
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Return the intersection of the two sets as a list
        return list(set1 & set2)
