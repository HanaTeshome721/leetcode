class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dfs(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            coldown=dfs(i+1,buy)    
            if buy:
                buyprofit=dfs(i+1,not buy) -prices[i]
                memo[(i,buy)]=max(coldown,buyprofit)
            else:
                sell=dfs(i+2,not buy) +prices[i]
                memo[(i,buy)]=max(coldown,sell) 
            return memo[(i,buy)]
        return dfs(0,True)               
