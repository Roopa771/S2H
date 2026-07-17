class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_value = -1
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                # find largest digit of nums[i]
                max1 = max(str(nums[i]))
                
                # find largest digit of nums[j]
                max2 = max(str(nums[j]))
                
                # check condition
                if max1 == max2:
                    max_value = max(max_value, nums[i] + nums[j])
        
        return max_value
                   