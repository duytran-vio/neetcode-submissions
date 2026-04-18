class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        INF = pow(2, 31) - 1
        dir = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))

        while len(q) != 0:
            u, v = q.popleft()
            for d in dir:
                x = u + d[0]
                y = v + d[1]
                if (x < 0 or y < 0 or x >= n or y >= m or grid[x][y] != INF or grid[x][y] == -1):
                    continue
                grid[x][y] = grid[u][v] + 1
                q.append((x, y))