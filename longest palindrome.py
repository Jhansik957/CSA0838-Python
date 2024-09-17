from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        length = 0
        odd_found = False
        
        for count in char_count.values():
            if count % 2 == 0:
                length += count  # Add all even counts
            else:
                length += count - 1  # Add the largest even part of the odd count
                odd_found = True  # Mark that we found at least one odd count
        
        # If any odd character exists, add 1 to the length to place it in the center
        if odd_found:
            length += 1
        
        return length
