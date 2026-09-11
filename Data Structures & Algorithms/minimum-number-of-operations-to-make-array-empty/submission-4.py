class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for _, value in freq.items():
            if value == 1:
                return -1
            res += math.ceil(value / 3)
        return res