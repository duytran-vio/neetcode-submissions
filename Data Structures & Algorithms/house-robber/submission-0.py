class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [0] * (n + 1)
        memo[1] = nums[0]

        for i in range(2, n + 1):
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i - 1])

        return memo[n]