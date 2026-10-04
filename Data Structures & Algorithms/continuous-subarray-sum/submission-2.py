class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pos = {}
        prefix_sum = 0
        pos[0] = -1
        for i in range(len(nums)):
            prefix_sum = (prefix_sum + nums[i]) % k
            if prefix_sum not in pos:
                pos[prefix_sum] = i
            elif i - pos[prefix_sum] > 1:
                return True
        return False