class Solution:
    def sortColors(self, nums: List[int]) -> None:

        left, right = 0, 0

        while right < len(nums):
            while left < len(nums) and nums[left] == 0:
                left += 1
            right = left + 1
            while right < len(nums) and nums[right] != 0:
                right += 1
            
            if right < len(nums):
                tmp = nums[right]
                nums[right] = nums[left]
                nums[left] = tmp
                left += 1
                right += 1  

        right = left + 1
        while right < len(nums):
            while left < len(nums) and nums[left] == 1:
                left += 1
            right = left + 1
            while right < len(nums) and nums[right] != 1:
                right += 1
            
            if right < len(nums):
                tmp = nums[right]
                nums[right] = nums[left]
                nums[left] = tmp
                left += 1
                right += 1  