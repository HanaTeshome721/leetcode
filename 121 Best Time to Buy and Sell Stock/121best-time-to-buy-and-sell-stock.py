class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      mxp=0
      l=0
      r=1
      while r<len(prices):
         if prices[r]-prices[l]>0:
            profit=prices[r]-prices[l]
            mxp=max(mxp,profit)
         else:
            l=r
         r+=1
      return mxp         
