class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(index: int, subset: List[int]):
            if index == n:
                res.append(subset.copy())
                return
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()
            backtrack(index + 1, subset)
        backtrack(0, [])
        return res