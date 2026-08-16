class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = neg = 0
        isPos, n = True, len(nums)
        res = []
        for i in range(n):
            if isPos:
                while pos < n and nums[pos] < 0:
                    pos += 1
                res.append(nums[pos])
                pos += 1
            else:
                while neg < n and nums[neg] > 0:
                    neg += 1
                res.append(nums[neg])
                neg += 1
            isPos = not isPos

        return res