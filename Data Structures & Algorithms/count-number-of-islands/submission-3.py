class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        q = deque([])
        n, m = len(grid), len(grid[0])
        dir = [-1, 0, 1, 0, -1]
        for i in range(0, n):
            for j in range(0, m):
                print(i, j)
                if grid[i][j] == '1':
                    q.append((i, j))
                    grid[i][j] = '0'
                    cnt += 1
                    while q:
                        u, v = q.pop()
                        for k in range(0, 4):
                            x = u + dir[k]
                            y = v + dir[k + 1]
                            if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == '1':
                                q.append((x, y))
                                grid[x][y] = '0'

        return cnt