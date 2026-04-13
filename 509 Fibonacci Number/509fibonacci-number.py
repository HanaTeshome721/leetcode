class Solution:
    def fib(self, n: int) -> int:
        # memo={}
        # def help(n):
        #     if n==1 or n==0:
        #         return n
        #     if n in memo:
        #         return memo[n]    
        #     memo[n]=help(n-1) + help(n-2)
        #     return memo[n]
        # return help(n)

        # dp=[0]*(n+1)
        # dp[0],dp[1]=0,1
        # for i in range(2,n+1):
        #     dp[i]=dp[i-1] +dp[i-2]
        # return dp[n]   

        fib=[0,1]
        for i in range(2,n+1):
            fib.append(fib[i-1]+fib[i-2])
        return fib[n]             