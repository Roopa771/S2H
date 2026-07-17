class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        dup = 0
        
        for i in nums:
            if i in s:
                dup = i
            else:
                s.add(i)
        
        for i in range(1, len(nums)+1):
            if i not in s:
                return [dup, i]