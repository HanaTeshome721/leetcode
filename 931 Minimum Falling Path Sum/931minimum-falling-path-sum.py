class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # memo={}
        # def dfs(i,j):
        #     if i>=n:
        #         return 0
        #     if j<0 or j>=n:
        #         return float("inf")
        #     if (i,j) in memo:
        #         return memo[(i,j)]    
        #     down=dfs(i+1,j)
        #     right=dfs(i+1,j+1)
        #     left=dfs(i+1,j-1)
        #     memo[(i,j)]=matrix[i][j] + min(down,right,left)
        #     return memo[(i,j)]
        # n=len(matrix)
        # res=float("inf")
        # for i in range(n):
        #     res=min(dfs(0,i),res)
        # return res 
        n=len(matrix)
        res=float("inf")
        for i in range(1,n):
            for j in range(n):
              left=matrix[i-1][j-1]  if j>0 else float("inf")
              right=matrix[i-1][j+1] if j+1<n else float("inf")
              up=matrix[i-1][j]  
              matrix[i][j]=matrix[i][j] + min(left,right,up)
        return min(matrix[-1])      

