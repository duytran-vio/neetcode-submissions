
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()

        for bitmap in range(1 << n):
            subset = [nums[j] for j in range(n) if (bitmap & (1 << j))]
            subset.sort()
            res.add(tuple(subset))
        
        return list(res)