class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       island=0
       row=len(grid)
       col=len(grid[0])
       direction=[(1,0),(-1,0),(0,1),(0,-1)] 
       def dfs(i,j):
        if not( 0<=i<row and 0<=j<col and grid[i][j]=="1"):
            return 
        grid[i][j]="0"
        for dr,dc in direction:
            nr=dr+i
            nc=dc+j
            dfs(nr,nc)
            

       for i in range(row):
         for j in range(col):
            if grid[i][j]=="1":
                island+=1
                dfs(i,j)
       return island 












    # def is_valid(self, grid, i, j):
    #     return i >=0 and i < len(grid) and j >= 0 and j < len(grid[0])
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     seen = set()
    #     def traverse(i, j):
    #         if not self.is_valid(grid, i, j):
    #             return

    #         if (i,j) in seen or grid[i][j] == "0":
    #             return
    #         seen.add((i,j))

    #         traverse(i, j-1)
    #         traverse(i, j+1)
    #         traverse(i-1, j)
    #         traverse(i+1, j)

    #     islands = 0
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if (i,j) not in seen and grid[i][j] == "1":
    #                 islands += 1
    #                 traverse(i,j)
        
    #     return islands








    #     row = len(grid)
    #     col = len(grid[0])
    #     directions = [(0,-1), (0,1), (1,0), (-1,0)]
        
    #     def bfs(r, c):
    #         queue = deque()
    #         queue.append((r, c))
    #         grid[r][c] = "0"
            
    #         while queue:
    #             cr, cc = queue.popleft()
                
    #             for dr, dc in directions:
    #                 nr = cr + dr
    #                 nc = cc + dc
                    
    #                 if (0 <= nr < row and 
    #                     0 <= nc < col and 
    #                     grid[nr][nc] == "1"):
                        
    #                     grid[nr][nc] = "0"
    #                     queue.append((nr, nc))
        
    #     island = 0
        
    #     for i in range(row):
    #         for j in range(col):
    #             if grid[i][j] == "1":
    #                 island += 1
    #                 bfs(i, j)
        
    #     return island
        