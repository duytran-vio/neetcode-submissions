class TimeMap:

    def __init__(self):
        self.H = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.H:
            self.H[key] = []
        self.H[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        print(self.H)
        if key not in self.H:
            return ""

        l, r = 0, len(self.H[key]) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if (self.H[key][mid][0] <= timestamp):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return "" if res == -1 else self.H[key][res][1]
