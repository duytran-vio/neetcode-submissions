class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)

        heap = []
        for num, freq in cnt.items():
            heapq.heappush(heap, (freq, num))

            if (len(heap) > k):
                heapq.heappop(heap)
        
        return [num for _, num in heap]