class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            for c in range(COLS):
                self.sumMat[r + 1][c + 1] = self.sumMat[r][c + 1] + self.sumMat[r + 1][c] - self.sumMat[r][c] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumMat[row2 + 1][col2 + 1] - self.sumMat[row1][col2 + 1] - self.sumMat[row2 + 1][col1] + self.sumMat[row1][col1]