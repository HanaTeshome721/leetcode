class Solution:
    def numDistinct(self, s: str, t: str) -> int:
    #     memo={}
    #     def dfs(i,j):
    #         if j==len(t):
    #             return 1
    #         if i==len(s):
    #             return 0
    #         if (i,j) in memo:
    #             return memo[(i,j)]    
    #         if s[i]==t[j]:
    #             memo[(i,j)]=dfs(i+1,j+1) + dfs(i+1,j)     
    #         else:
    #             memo[(i,j)]=dfs(i+1,j)
    #         return memo[(i,j)]
    #     return dfs(0,0)  











        
    #     @cache
    #     def dfs(i, j):
    #         if i < 0: return 1
    #         if j < i: return 0
    #         ans = dfs(i, j - 1) 
    #         if t[i] == s[j]:
    #             ans += dfs(i - 1, j - 1) 
    #         return ans

    #     m, n = len(t), len(s)
    #     return dfs(m - 1, n - 1)  



    # m, n = len(s), len(t)
    # dp = [0] * (n + 1)
    # dp[0] = 1
    
    # for i in range(1, m + 1):
    #     prev = 1  
    #     for j in range(1, n + 1):
    #         temp = dp[j]  
    #         if s[i-1] == t[j-1]:
    #             dp[j] = prev + dp[j]
    #         else:
    #             dp[j] = dp[j]
    #         prev = temp
    
    # return dp[n]             









        m,n=len(s) ,len(t)
        dp=[[0] *(n+1) for i in range(m+1)]
        
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[m][n]                