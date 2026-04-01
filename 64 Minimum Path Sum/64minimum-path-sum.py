class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # row=len(grid)
        # col=len(grid[0])
        # res=[[float("inf") ]*(col+1) for r in range(row+1)]
        # res[row-1][col]=0

        # for r in range(row-1,-1,-1):
        #     for c in  range(col-1 ,-1,-1):
        #         res[r][c]=grid[r][c] + min(res[r+1][c] , res[r][c+1])
        # return res[0][0]         

        # row=len(grid)
        # col=len(grid[0])
        # memo={}
        # def dfs(r,c):
        #     if r==row-1 and c==col-1:
        #         return grid[r][c]
        #     if r>=row or c>=col:
        #         return float("inf")
        #     if (r,c) in memo:
        #         return memo[(r,c)]
        #     down=dfs(r+1,c)            
        #     right=dfs(r,c+1)       
        #     memo[(r,c)]=grid[r][c] + min(down,right)
        #     return memo[(r,c)]
        # return dfs(0,0)          

            if not grid or not grid[0]:
                return 0
            m=len(grid)
            n=len(grid[0])
            d=[0 for _ in range(n)]
            d[0]=grid[0][0]
            for j in range(1,n):
                d[j]=d[j-1] +grid[0][j]

            for i in range(1,m):
                d[0]+=grid[i][0] 

                for j in range(1,n):
                    d[j]=min(d[j] , d[j-1]) + grid[i][j]
            return d[n-1]                
