# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Assuming there is a guess API that we need to simulate
def guess(num: int) -> int:
    # This is a dummy implementation for illustration purposes
    picked_number = 6  # You can replace this with the actual number to guess
    if num < picked_number:
        return 1
    elif num > picked_number:
        return -1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        # Binary search to find the correct number
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            
            if result == 0:
                return mid  # We found the number
            elif result == -1:
                right = mid - 1  # The guessed number is too high
            else:
                left = mid + 1  # The guessed number is too low

        return -1  # This line should never be reached if the guess is guaranteed to be valid
