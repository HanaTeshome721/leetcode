class Solution:
    def hIndex(self, citations: List[int]) -> int:
            # l=h=0
            # n=len(citations)
            # r=n-1
            # while l<=r:
            #     m=(l+r)//2
            #     if citations[m]>=n-m:
            #         h=n-m
            #         r=m-1
            #     else:
            #         l=m+1
            # return h   

           n=len(citations)
           r=n
           l=0
           def check(m):
              return citations[n-m]>=m
           while l<r:
                m=l+(r-l+1)//2
                if check(m):
                    l=m
                else:
                    r=m-1
           return l

           