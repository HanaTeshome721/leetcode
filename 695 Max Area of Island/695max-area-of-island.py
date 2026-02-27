class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       def inbound(i,j):
         if  i<0 or j<0 or i>=row or j >=col:
            return False
         else:
            return True   
       def dfs(i,j):
        if  grid[i][j]==0 or not inbound(i,j):
            return 0
        grid[i][j]=0    
        total=1
        for dr,dc in direction:
            nr=dr+i
            nc=dc+j
            if inbound(nr,nc) and grid[nr][nc]:
                total+=dfs(nr,nc)
        return total


       direction=[(1,0),(-1,0),(0,1),(0,-1)] 
       row=len(grid)
       col=len(grid[0])
       mx=0
       for i in range(row):
         for j in range(col):
            if grid[i][j]:
               v=dfs(i,j) 
               mx=max(v,mx)
       return mx        