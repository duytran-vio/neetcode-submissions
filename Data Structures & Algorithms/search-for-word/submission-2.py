class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, k = len(board), len(board[0]), len(word)
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        step = [[k + 1] * m for _ in range(n)]
        def dfs(u, v, index) -> bool:
            if index == k:
                return True
            if u < 0 or u >= n or v < 0 or v >= m or step[u][v] != k + 1 or board[u][v] != word[index]:
                return False
            
            step[u][v] = index
            if dfs(u - 1, v, index + 1) or dfs(u, v - 1, index + 1) or dfs(u + 1, v, index + 1) or dfs(u, v + 1, index + 1):
                    return True
            step[u][v] = k + 1
            return False

        for i in range(n):
            for j in range(m):
                    if dfs(i, j, 0):
                        return True
                
        return False