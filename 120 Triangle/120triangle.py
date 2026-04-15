class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
       dp=[0]*(len(triangle) +1)
       for row in triangle[::-1]:
         for i,r in enumerate(row):
            dp[i]=r + min(dp[i] , dp[i+1])
       return dp[0]          