class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # row=len(matrix)
        # column=len(matrix[0])
        # t=[[0]*row for _  in range(column)]
        # for r in range(row):
        #     for c in range(column):
        #         t[c][r]=matrix[r][c]
        # return t   


        # ROWS, COLS = len(matrix), len(matrix[0])
        # new_matrix = [[] for _ in range(COLS)]
        # for c in range(COLS):
        #     for r in range(ROWS):
        #         new_matrix[c].append(matrix[r][c])
        # return new_matrix


        # rows = len(matrix)
        # cols = len(matrix[0])
        # result = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
        # return result
        row=len(matrix)
        col=len(matrix[0])
        return [[matrix[i][j] for i in range(row)] for j in range(col)]









