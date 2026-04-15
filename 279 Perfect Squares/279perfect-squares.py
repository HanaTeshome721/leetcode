class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n]*(n+1)
        dp[0]=0
        for t in range(n+1):
            for s in range(t+1):
                sq=s*s
                if t-sq<0:
                    break
                dp[t]=min(dp[t] , 1+dp[t-sq])
        return dp[n]            
 


        #   memo = {}

        # def dfs(t):
        #     if t == 0:
        #         return 0
        #     if t in memo:
        #         return memo[t]

        #     res = float('inf')

        #     s = 1
        #     while s * s <= t:
        #         sq = s * s
        #         res = min(res, 1 + dfs(t - sq))
        #         s += 1

        #     memo[t] = res
        #     return res

        # return dfs(n)     







        # dp = 1<<n
        # g = {i**2 for i in range(1, int(n**(1/2)+1))}
        # step = 0
        # while dp & 1 != 1:
        #     tmp = dp
        #     for i in g:
        #         dp |= tmp >> i
        #     step += 1
        # return step