class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mp = {}
        ans = -1

        for num in nums:
            digit_sum = 0
            temp = num

            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            if digit_sum in mp:
                ans = max(ans, num + mp[digit_sum])
                mp[digit_sum] = max(mp[digit_sum], num)
            else:
                mp[digit_sum] = num

        return ans