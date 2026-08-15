class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False] * n
        res = []
        def dfs(permutation):
            per_len = len(permutation)
            if per_len == n:
                res.append(permutation.copy())
                return
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    permutation.append(nums[i])
                    dfs(permutation)
                    permutation.pop()
                    visited[i] = False
        dfs([])
        return res