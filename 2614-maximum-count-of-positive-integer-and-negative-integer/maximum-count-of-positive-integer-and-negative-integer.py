class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nc=0
        pc=0
        for i in range(len(nums)):
            if(nums[i]>0):
                pc=pc+1
            elif(nums[i]<0):
                nc=nc+1
        if(pc>nc):
            return pc
        else:
            return nc
        

            
        