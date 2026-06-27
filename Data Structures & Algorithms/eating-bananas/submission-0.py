class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        l, r = 1, max_rate
        res = 1
        while l <= r:
            mid = (l + r) // 2
            eat_hour = self.getEatHour(mid, piles)
            if eat_hour <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

    def getEatHour(self, rate: int, piles: List[int]) -> int:
        hour = 0
        for pile in piles:
            hour += (pile + rate - 1) // rate
        return hour