class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        pre = suf = 1
        
        for i in range(n):
            ans[i] *= pre
            pre *= nums[i]
            ans[-1 - i] *= suf
            suf *= nums[-1 - i]
        
        return ans
