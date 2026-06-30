class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        sum = 0
        res = len(nums) + 1

        while r < len(nums):
            while r < len(nums) and sum < target:
                sum += nums[r]
                r += 1

            if sum < target:
                break

            while l < r and sum >= target:
                sum -= nums[l]
                l += 1

            # [l - 1, r) ==> subarray has sum >= target, minimum length
            res = min(res, r - l + 1)
        return res if res != len(nums) + 1 else 0