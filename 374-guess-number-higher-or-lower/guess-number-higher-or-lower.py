# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)
            
            if res == 0:   # Found the number
                return mid
            elif res == -1:  # Guess is too high
                high = mid - 1
            else:           # Guess is too low
                low = mid + 1
