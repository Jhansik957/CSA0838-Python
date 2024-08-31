1 maximum water in a container
def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        water = min(height[left], height[right]) * width
        max_water = max(max_water, water)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water

height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))  


2 group anagrams
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))



3merging intervals
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    
    for interval in intervals:

        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

intervals = [[1,0],[2,3],[5,4],[6,7],[8,2]]
print(merge(intervals))  
