class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        min_heap = []
        heapq.heapify(min_heap)

        for interval in intervals:
            if len(min_heap) == 0:
                heapq.heappush(min_heap, interval.end)
                continue
            if min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
        return len(min_heap)