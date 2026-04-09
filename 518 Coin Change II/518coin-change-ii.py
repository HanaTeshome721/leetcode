class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    #   memo={}  
    #   def dfs(i,cum):
    #     if cum ==amount:
    #         return 1
    #     if i>=len(coins) or cum > amount:
    #         return 0
    #     if (i,cum) in memo:
    #         return memo[(i,cum)]    
    #     skip=dfs(i+1,cum)
    #     use=dfs(i,cum+coins[i])
    #     memo[(i,cum)]=skip +use
    #     return memo[(i,cum)]
    #   return dfs(0,0)          
   

    #   dp=[[0] *(len(coins)+1) for i in range(amount+1)]
    #   dp[0]=[1]*(len(coins)+1)
    #   for a in range(1,amount+1):
    #         for c in range(len(coins)-1,-1,-1):
    #             dp[a][c]=dp[a][c+1]
    #             if a-coins[c]>=0:
    #                 dp[a][c] +=dp[a-coins[c]][c]   
    #   return dp[amount][0]                     


      dp=[0]*(amount+1)
      dp[0]=1
      for c in range(len(coins)-1,-1,-1):
        nextd=[0]*(amount+1)
        nextd[0]=1
        for a in range(1,amount+1):
            nextd[a]=dp[a]
            if a-coins[c]>=0:
                nextd[a]+=nextd[a-coins[c]]
        dp=nextd
      return dp[amount]      



