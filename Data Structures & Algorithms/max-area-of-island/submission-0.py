class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        q = deque()
        res = 0
        n, m = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    q.append((r, c))
                    grid[r][c] = 0
                    area = 0
                    while q:
                        u, v = q.popleft()
                        area += 1
                        for dir in dirs: 
                            x, y = u + dir[0], v + dir[1]
                            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                                continue
                            q.append((x, y))
                            grid[x][y] = 0
                    res = max(res, area)
        return res