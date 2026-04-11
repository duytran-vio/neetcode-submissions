
class Solution:
    def robSub(self, nums: List[int]) -> int:
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
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        rob_adj_last = self.robSub(nums[:-1])
        rob_skip_first_and_last_house = self.robSub(nums[1:-2])
        return max(rob_adj_last, rob_skip_first_and_last_house + nums[-1])