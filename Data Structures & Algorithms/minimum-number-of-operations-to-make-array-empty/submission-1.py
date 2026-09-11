class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        res = 0
        for _, value in freq.items():
            if value == 1:
                return -1
            res += value // 3 if value % 3 == 0 else value // 3 + 1
        return res