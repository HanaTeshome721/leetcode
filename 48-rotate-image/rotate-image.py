class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lr=len(matrix)
           
        for i in range(lr):
            for j in range(i+1,lr):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]

        for r in matrix:
            r.reverse()            