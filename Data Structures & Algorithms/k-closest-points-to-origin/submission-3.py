class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            square_distance = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(max_heap, (-square_distance, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        while max_heap:
            dist, point = heapq.heappop(max_heap)
            res.append(point)
        return res