class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n 
        while(k>0):
            k=k-1
            t=nums.pop(-1)
            nums.insert(0,t) 