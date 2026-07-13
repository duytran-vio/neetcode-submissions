class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_prefix_sum_q = deque([(0, -1)])
        n = len(nums)
        prefix_sum = 0
        res = nums[0]
        for i in range(2 * len(nums)):
            prefix_sum += nums[i % n]
            while min_prefix_sum_q and min_prefix_sum_q[0][1] + n < i:
                min_prefix_sum_q.popleft()
            
            res = max(res, prefix_sum - min_prefix_sum_q[0][0])
            while min_prefix_sum_q and min_prefix_sum_q[-1][0] > prefix_sum:
                min_prefix_sum_q.pop()

            min_prefix_sum_q.append((prefix_sum, i))
        return res
            