class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            # Add current subset to result
            result.append(path[:])
            
            # Explore further elements
            for i in range(start, len(nums)):
                # Include nums[i]
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # backtrack

        backtrack(0, [])
        return result