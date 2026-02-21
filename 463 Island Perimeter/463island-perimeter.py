class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
       visit=set()
       def dfs(i,j):
         if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]==0:
            return 1
         if (i,j) in visit:
            return 0
         visit.add((i,j))  
         perm=dfs(i+1,j)      
         perm+=dfs(i-1,j)      
         perm+=dfs(i,j+1)      
         perm+=dfs(i,j-1)  
         return perm
       for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i,j)





        # rows, cols = len(grid), len(grid[0])
        # perimeter = 0
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == 1:
        #             perimeter += 4
        #             if i > 0 and grid[i - 1][j] == 1:
        #                 perimeter -= 2
        #             if j > 0 and grid[i][j - 1] == 1:
        #                 perimeter -= 2
        # return perimeter        
        


        
        # direction=[(0,1),(1,0),(-1,0),(0,-1)]
        # visited=[[False]*len(grid[0]) for _ in range(len(grid))]

        # def inbound(r,c):
        #     return 0<=r<len(grid) and 0<=c<len(grid[0])
        # def dfs(i,j):
        #     if not inbound(i,j) or grid[i][j]==0:
        #         return 1
        #     if visited[i][j]:
        #         return 0
        #     visited[i][j]=True

        #     perim=0
        #     for dr, dc in direction:
        #         perim+=dfs(i+dr,j+dc)
        #     return perim

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j]:
        #             return dfs(i,j)         

              
