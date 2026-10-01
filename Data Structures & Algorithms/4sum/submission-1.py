class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadSet = set()
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                remain = target - nums[i] - nums[j]
                l, r = j + 1, n - 1
                while l < r:
                    if nums[l] + nums[r] < remain:
                        l += 1
                    elif nums[l] + nums[r] > remain:
                        r -= 1
                    else:
                        quadruplet = (nums[i], nums[j], nums[l], nums[r])
                        if quadruplet not in quadSet:
                            quadSet.add(quadruplet)
                        l += 1
                        r -= 1
        return list(quadSet)