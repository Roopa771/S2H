class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []

        for i in nums:
            s.add(i)

        for i in range(1, len(nums)+1):
            if i not in s:
                ans.append(i)

        return ans