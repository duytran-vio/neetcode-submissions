class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0] * 2 for _ in range(n + 1)]

        for i in range(1, n + 1):
            index = i - 1
            f[i][0] = max(f[i - 1][0], f[i - 1][1])
            f[i][1] = f[i - 1][0] + nums[index]
        return max(f[n][0], f[n][1])