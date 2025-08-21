class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        squer=defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if( board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in squer[(r//3 ,c//3)]):            
                   return False
                rows[r].add(board[r][c])   
                cols[c].add(board[r][c])   
                squer[(r//3,c//3)].add(board[r][c])
        return True 

        #  to get the columns
        #  for i in range(9):
        #     s=set()
        #       for j in range(9):
        #      #  item =board[j][i]  #FOR board[i][j],raw
        #           if item in s:
        #             return False
        #           elif item not '.':
        #             s.add(item)  
        #   start=[(0,0)(0,3),(0,6)]
        #         (3,0)(3,3),(3,6)]
        #         (6,0)(6,3),(6,6)]

        #    for i,j in start:
        #     s=set()
        #     for row in range(i,i+3):
        #         for col in range(j, j+3):
        #             value= board[row][col]
        #             if item in s:
        #                 return False
        #             else:
        #                 s.add(item)    