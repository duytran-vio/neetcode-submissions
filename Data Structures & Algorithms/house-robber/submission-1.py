class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        current_value = 0
        adj_value = nums[0]
        skip_one_value = 0

        for i in range(1, n):
            current_value = max(adj_value, skip_one_value + nums[i])
            skip_one_value, adj_value = adj_value, current_value

        return current_value