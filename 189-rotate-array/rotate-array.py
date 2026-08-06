class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # handle large k
        
        # Helper function to reverse
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # Step 1: Reverse whole array
        reverse(0, n - 1)
        
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        
        # Step 3: Reverse remaining elements
        reverse(k, n - 1)