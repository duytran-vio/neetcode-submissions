class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        sum = 0
        res = n + 1

        while r < n:
            while r < n and sum < target:
                sum += nums[r]
                r += 1

            if sum < target:
                break

            while l < r and sum >= target:
                sum -= nums[l]
                l += 1

            # [l - 1, r) ==> subarray has sum >= target, minimum length
            res = min(res, r - l + 1)
        return res if res != n + 1 else 0