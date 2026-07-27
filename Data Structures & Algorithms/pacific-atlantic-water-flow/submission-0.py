class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        pacificReach = [[0 for _ in range(m)] for _ in range(n)]
        atlanticReach = [[0 for _ in range(m)] for _ in range(n)]


        q = deque([])
        for j in range(m):
            q.append((0, j))
            pacificReach[0][j] = 1
        for i in range(n):
            q.append((i, 0))
            pacificReach[i][0] = 1
        pacificReach = self.bfs(heights, q, pacificReach, 0)


        q = deque([])
        for j in range(m):
            q.append((n - 1, j))
            atlanticReach[n - 1][j] = 1
        for i in range(n):
            q.append((i, m - 1))
            atlanticReach[i][m - 1] = 1
        atlanticReach = self.bfs(heights, q, atlanticReach, 1)

        res = []
        for i in range(n):
            for j in range(m):
                if pacificReach[i][j] == 1 and atlanticReach[i][j] == 1:
                    res.append([i, j])
        return res

    def bfs(self, heights: List[List[int]], q: deque, canReach: List[List[int]], bitIndex: int) -> List[List[int]]:
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        n, m = len(heights), len(heights[0])
        while q:
            u, v = q.pop()
            for dir in dirs:
                x, y = u + dir[0], v + dir[1]
                if x >= 0 and x < n and y >= 0 and y < m and canReach[x][y] == 0 and heights[u][v] <= heights[x][y]:
                    canReach[x][y] = 1
                    q.append((x, y))

        return canReach
        