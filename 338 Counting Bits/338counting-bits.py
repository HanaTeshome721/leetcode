class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp=[0]*(n+1)
        # dp[0]=0
        # offset=1
        # for i in range(1,n+1):
        #     if offset*2==i:
        #         offset=i
        #     dp[i]=1+dp[i-offset]    
        # return dp    

        # ans = []
        # for i in range(n + 1):
        #     ans.append(bin(i).count('1'))
        # return ans



        ans=[0]*(n+1)
        for i in range(1,n+1):
            ans[i]=ans[i>>1] + (i&1)
        return ans    