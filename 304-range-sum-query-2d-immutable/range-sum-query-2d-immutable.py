class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rw=len(matrix)
        cl=len(matrix[0])
        self.pref=[[0]*(cl+1) for _ in range(rw+1)]

        for r in range(rw):
            for c in range(cl):
                self.pref[r][c]=self.pref[r-1][c] +self.pref[r][c-1]-self.pref[r-1][c-1] +matrix[r][c] 


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pref[row2][col2] -self.pref[row2][col1-1]-self.pref[row1-1][col2] + self.pref[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)