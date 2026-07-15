class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        
        for n in nums:
            digits = len(str(n))
            
            if digits % 2 == 0:
                c += 1
        
        return c