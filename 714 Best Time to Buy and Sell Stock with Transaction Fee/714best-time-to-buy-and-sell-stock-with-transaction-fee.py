class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
       memo={}

       def dfs(i,buy):
            if i ==len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            if buy:
                buys= -prices[i] + dfs(i+1,0)
                sell=dfs(i+1,1) 
                profit=max(sell,buys)
            else:
                sell=prices[i]-fee +dfs(i+1,1)
                buys=dfs(i+1,0)
                profit=max(sell,buys) 
            memo[(i,buy)]=profit
            return memo[(i,buy)]
       return dfs(0,1)             