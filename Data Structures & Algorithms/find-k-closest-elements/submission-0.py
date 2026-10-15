class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dis = defaultdict(list)
        maxDistance = abs(arr[0] - x)
        for e in arr:
            distance = abs(x - e)
            dis[distance].append(e)
            maxDistance = max(distance, maxDistance)

        cnt = ptr = 0
        res = []
        while cnt < k:
            while ptr < maxDistance and len(dis[ptr]) == 0:
                ptr += 1
            for i in range(min(k - cnt, len(dis[ptr]))):
                cnt += 1
                res.append(dis[ptr][i])
            ptr += 1
        res.sort()
        return res

        