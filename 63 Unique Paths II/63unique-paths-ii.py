class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        memo={}
        def dfs(i,j):
            if( i,j)==(n-1,m-1) and not obstacleGrid[i][j]:
                return 1
            if i==n or j==m:
                return 0    
            if obstacleGrid[i][j]:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=dfs(i+1,j) + dfs(i,j+1)
            return memo[(i,j)]
        return dfs(0,0)                