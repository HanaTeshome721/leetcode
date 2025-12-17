class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # l=max(weights)
        # r=sum(weights)
        # res=r
        # def can(m):
        #    ship=1
        #    curcap=m
        #    for i in weights:
        #      if curcap-i <0:
        #         ship+=1
        #         curcap=m
        #      curcap-=i   
        #    return ship<=days
        # while l<=r:
        #     m=(l+r)//2
        #     if can(m):
        #         res=min(res,m)
        #         r=m-1    
        #     else:
        #         l=m+1
        # return res      




        # def check(c): 
        #     cnt = 1
        #     cap = 0
        #     for i in a:
        #         if cap + i > c:
        #             cnt += 1
        #             cap = i
        #             if cnt > days:
        #                 return False
        #         else:
        #             cap += i
        #     return True
        # l, r = max(a), max(a) * ceil(len(a) / days)
        # ans = r
        # while l <= r:
        #     m = (l+r)//2
        #     if check(m):
        #         ans = min(ans, m)
        #         r = m - 1
        #     else:
        #         l = m +1
        # return ans






        low=max(weights)
        high=sum(weights)

        while low<=high:
            m=(low+high)//2
            curday=1
            curw=0
            for w in weights:
                if curw+w<=m:
                    curw+=w
                else:
                    curw=w
                    curday+=1
            if curday<=days:
                high=m-1
            else:
                low=m+1
        return low                        
     