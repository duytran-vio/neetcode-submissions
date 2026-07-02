import bisect
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sumLength = len(nums1) + len(nums2)

        if sumLength % 2:
            return self.find(nums1, nums2, sumLength // 2)
        else:
            median1 =  self.find(nums1, nums2, sumLength // 2)
            median2 =  self.find(nums1, nums2, sumLength // 2 - 1)
            return (median1 + median2) / 2

    def find(self, nums1: List[int], nums2: List[int], k: int) -> int:
        value = self.findIn(nums1, nums2, k)
        if value == -1:
            value = self.findIn(nums2, nums1, k)
        return value
    
    def findIn(self, nums1: List[int], nums2: List[int], k: int) -> int:
        l, r = 0, len(nums1)-1
        while l <= r:
            mid = (l + r) // 2
            cnt_lower_nums2 = bisect.bisect_left(nums2, nums1[mid])
            cnt_lower_include_equal_nums2 = bisect.bisect_right(nums2, nums1[mid])
            if cnt_lower_nums2 <= k - mid and k - mid <= cnt_lower_include_equal_nums2:
                return nums1[mid]
            elif cnt_lower_nums2 < k - mid:
                l = mid + 1
            else:
                r = mid - 1
        return -1