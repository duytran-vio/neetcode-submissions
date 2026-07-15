
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq = {}
        maximum = nums[0]
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            maximum = max(maximum, num)

        res = maximum
        while k > 0:
            if maximum in freq:
                res = maximum
                k -= freq[maximum]
            maximum -= 1
        return res