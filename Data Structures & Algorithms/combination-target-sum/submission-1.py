class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index: int, remain: int, combination: List[int]):
            if remain == 0:
                res.append(combination.copy())
                return
            for i in range(index, len(nums)):
                if remain >= nums[i]:
                    combination.append(nums[i])
                    dfs(i, remain - nums[i], combination)
                    combination.pop()
                else:
                    return
        dfs(0, target, [])
        return res