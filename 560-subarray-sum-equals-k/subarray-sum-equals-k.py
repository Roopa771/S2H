class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0
        prefix = {0: 1}

        for num in nums:
            prefixSum += num

            if prefixSum - k in prefix:
                count += prefix[prefixSum - k]

            prefix[prefixSum] = prefix.get(prefixSum, 0) + 1

        return count