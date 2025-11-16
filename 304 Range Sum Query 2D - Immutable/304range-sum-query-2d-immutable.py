class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row=len(matrix)
        self.col=len(matrix[0])
        self.perif=[[0]*(self.col+1) for _ in range( self.row+1)]
        for r in range(self.row):
            for c in range(self.col):
                self.perif[r][c]=self.perif[r][c-1]+self.perif[r-1][c]-self.perif[r-1][c-1]+matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.perif[row2][col2]-self.perif[row1-1][col2]-self.perif[row2][col1-1]+self.perif[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)