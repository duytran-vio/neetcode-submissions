class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt_sum = {}
        cnt_sum[0] = 1
        res = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            left_prefix_sum = prefix_sum - k
            res += cnt_sum.get(left_prefix_sum, 0)
            cnt_sum[prefix_sum] = cnt_sum.get(prefix_sum, 0) + 1

        return res