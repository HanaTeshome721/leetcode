class Solution:
    def tribonacci(self, n: int) -> int:
        # memo={}
        # def help(n):
        #     if n==0:
        #         return 0
        #     if n<=2:
        #         return 1
        #     if n in memo:
        #         return memo[n]
        #     memo[n]=help(n-1) + help(n-2) + help(n-3)
        #     return memo[n]
        # return help(n)            

        # t=[0,1,1]
        # if n<3:
        #     return t[n]
        # for i in range(3,n+1):
        #     tem=t[0]+t[1]+t[2]
        #     t[0]=t[1]
        #     t[1]=t[2]
        #     t[2]=tem
        # return t[2]  
        if n==0:
            return 0
        if n<=2:
            return  1   
        dp=[0]*(n+1)
        dp[0]=0  
        dp[1]=1  
        dp[2]=1

        for i in range(3,n+1):
            dp[i]=dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]      
     





