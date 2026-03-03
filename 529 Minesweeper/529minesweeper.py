class Solution:
        
        def getmin(self,board,x,y):
            nummin=0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if 0<=i<len(board)and 0<=j<len(board[0]) and board[i][j]=="M":
                        nummin+=1
            return nummin


        def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
            if not board:
                return board
            r,c=click
            if board[r][c]=="M":
                board[r][c]="X"
                return board

            else:
                num=self.getmin(board,r,c)
                if num:
                    board[r][c]=str(num)
                    
                else:
                    board[r][c]="B"    
                    for i in range(r-1,r+2):
                      for j in range(c-1,c+2):
                        if 0<=i<len(board)and 0<=j<len(board[0]) and board[i][j]!="B":
                             self.updateBoard(board,[i,j])
            return board   

    #     numMine=0
    #     for r in range(x-1,x+2):
    #        for c in range(y-1,y+2):
    #         if r>=0 and r<len(board) and c >=0 and c<len(board[0]) and board[r][c]=="M":
    #             numMine+=1
    #     return numMine    


    # def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    #     if not board:
    #       return board
    #     x,y=click  
    #     if board[x][y]=="M":
    #         board[x][y]="X"
    #     else:
    #         numMine=self.getMineagesent(board,x,y) 
    #         if numMine:
    #            board[x][y]=str(numMine)
    #         else:
    #          board[x][y]="B"    
    #          for r in range(x-1,x+2):
    #            for c in range(y-1,y+2):
    #             if r>=0  and r<len(board) and c>=0 and c<len(board[0]) and board[r][c]!='B':
    #                 self.updateBoard(board, [r,c])
    #     return board     







     
        # m, n = len(board), len(board[0])
        # r, c = click

        # directions = [
        #     (-1, -1), (-1, 0), (-1, 1),
        #     (0, -1),          (0, 1),
        #     (1, -1),  (1, 0), (1, 1)
        # ]

        
        # if board[r][c] == 'M':
        #     board[r][c] = 'X'
        #     return board

    
        # def dfs(x, y):
           
        #     mine_count = 0
        #     for dx, dy in directions:
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
        #             mine_count += 1

            
        #     if mine_count > 0:
        #         board[x][y] = str(mine_count)
        #         return

           
        #     board[x][y] = 'B'

            
        #     for dx, dy in directions:
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'E':
        #             dfs(nx, ny)

        # dfs(r, c)
        # return board







        # rows = len(board)
        # cols = len(board[0])
        # DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # visited = [[False] * cols for _ in range(rows)]

        # queue = deque()
        # queue.append((click[0], click[1]))
        # visited[click[0]][click[1]] = True
        # while queue:
        #     r, c = queue.popleft()
        #     if board[r][c] == 'M':
        #         board[r][c] = 'X'
        #         break
        #     elif board[r][c] == 'E':
        #         digit = 0
        #         nextPos = []
        #         for dr, dc in DIRS:
        #             nr, nc = r + dr, c + dc
        #             if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
        #                 nextPos.append((nr, nc))
        #                 if board[nr][nc] == 'M':
        #                     digit += 1
        #         if digit == 0:
        #             board[r][c] = 'B'
        #             for i, j in nextPos:
        #                 queue.append((i, j))
        #                 visited[i][j] = True
        #         else:
        #             board[r][c] = str(digit)
        
        # return board

























       

      