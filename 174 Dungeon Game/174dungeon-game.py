class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # n=len(dungeon)
        # m=len(dungeon[0])
        # memo={}
        # def dfs(i,j):
        #     if (i,j)==(n-1,m-1):
        #         return max(1,1-dungeon[i][j])
        #     if i>=n or j>=m:
        #         return float('inf')    
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     down=dfs(i+1,j)
        #     right=dfs(i,j+1)    
        #     memo[(i,j)]=max(1,min(down,right) - dungeon[i][j])
        #     return memo[(i,j)]
        # return dfs(0,0)  


        n=len(dungeon)
        m=len(dungeon[0])
        dp=[[float("inf")]*(m+1) for i in range(n+1)]
        dp[n-1][m]=1
        dp[n][m-1]=1 

        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                need=min(dp[r+1][c] , dp[r][c+1])- dungeon[r][c]
                dp[r][c]=max(1,need)
        return dp[0][0]               

        