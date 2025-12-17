class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            m=(l+r)//2
            k=0
            for p in piles:
                k+=ceil(p/m)
            if k<=h:
                ans=min(ans,m)
                r=m-1
            else:
                l=m+1
        return ans                



        # l=1
        # r=sum(piles)
        # ans=r
        # def can(m):
        #     k=0
        #     for n in piles:
        #         # (n+m-1)//m
        #          k+=ceil(n/m)
        #     return k<=h
        # while l<=r:
        #     m=(l+r)//2
        #     if can(m):
        #         ans=min(ans,m)
        #         r=m-1
        #     else:
        #         l=m+1
        # return ans   