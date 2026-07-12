
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        max_heap = []
        min_heap = []
        heapq.heapify(min_heap)
        heapq.heapify(max_heap)
        l = 0
        for r in range(len(nums)):
            heapq.heappush(min_heap, (nums[r], r))
            heapq.heappush(max_heap, (-nums[r], r))

            while True:
                max_value = -self.getValue(max_heap, l, r)
                min_value = self.getValue(min_heap, l, r)
                biggest_abs_dif = max_value - min_value
                if biggest_abs_dif <= limit:
                    break
                l += 1

            res = max(res, r - l + 1)
        return res


    def getValue(self, heap, l: int, r: int) -> int:
        while True:
            value, index = heapq.heappop(heap)
            if l <= index and index <= r:
                break
        heapq.heappush(heap, (value, index))
        return value