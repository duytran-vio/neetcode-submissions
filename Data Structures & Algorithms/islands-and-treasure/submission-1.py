class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        n, m = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        INF = 2147483647
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append([r, c, 0])

        while q:
            u, v, dis = q.popleft()
            for dir in dirs:
                x, y = u + dir[0], v + dir[1]
                if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != INF or grid[x][y] == -1:
                    continue
                grid[x][y] = dis + 1
                q.append([x, y, dis + 1])