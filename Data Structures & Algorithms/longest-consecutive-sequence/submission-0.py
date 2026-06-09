class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcis = {}
        res = 0
        nums.sort()
        for num in nums:
            lcis[num] = lcis.get(num - 1, 0) + 1
            res = max(res, lcis[num])

        return res    