class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rl=len(matrix)
        cl=len(matrix[0])

        tp=[ [0]*rl for i in range(cl) ]
        print(tp)
        for i in range(rl):
            for j in range(cl):
                tp[j][i]=matrix[i][j]
        return tp        