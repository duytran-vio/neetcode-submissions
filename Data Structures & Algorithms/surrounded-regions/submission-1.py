
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        isSurrounded = [[True] * COLS for _ in range(ROWS)]

        q = deque([])
        for i in range(ROWS):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][COLS - 1] == "O":
                q.append((i, COLS - 1))
        for j in range(COLS):
            if board[0][j] == "O":
                q.append((0, j))
            if board[ROWS - 1][j] == "O":
                q.append((ROWS - 1, j))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q:
            u, v = q.pop()
            isSurrounded[u][v] = False
            for dir in directions:
                x, y = u + dir[0], v + dir[1]
                if x >= 0 and x < ROWS and y >= 0 and y < COLS and board[x][y] == "O" and isSurrounded[x][y]:
                    q.append((x, y))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and isSurrounded[i][j]:
                    board[i][j] = "X"
