class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: return True
        intervals.sort(key=lambda interval: interval.start)
        maxEnd = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < maxEnd:
                return False
            maxEnd = max(maxEnd, intervals[i].end)
                       
        return True