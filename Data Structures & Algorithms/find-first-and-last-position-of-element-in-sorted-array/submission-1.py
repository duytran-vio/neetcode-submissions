class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        start, end = -1, -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    start = mid
                r = mid - 1
            else:
                l = mid + 1

        if start == -1:
            return [-1, -1]

        l, r = start, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    end = mid
                l = mid + 1
            else:
                r = mid - 1

        return [start, end]
