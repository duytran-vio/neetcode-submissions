class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)

        # heap = []
        # for num, freq in cnt.items():
        #     heapq.heappush(heap, (freq, num))

        #     if (len(heap) > k):
        #         heapq.heappop(heap)

        freq = [[] for _ in range(len(nums) + 1)]
        for num, frequency in cnt.items():
            freq[frequency].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                k -= 1
                if (k == 0):
                    return res
        
        return res