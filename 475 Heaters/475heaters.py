import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # houses.sort()
        # heaters.sort()
        # ans=float('-inf')
        # for house in houses:
            
        #     ind=bisect.bisect_left(heaters,house)
        #     ld=house-heaters[ind-1] if ind>0 else float('inf')
        #     rd=heaters[ind]-house if ind<len(heaters) else float('inf')
        #     mn=min(ld,rd)
        #     ans=max(mn,ans)
        # return ans    

        # houses.sort()
        # heaters.sort()

        # def closedistance(house):
        #     l,r=0,len(heaters)-1
        #     best=float('inf')
        #     while l<=r:
        #         m=(l+r)//2
        #         best=min(best,abs(heaters[m] - house))
        #         if heaters[m]<house:
        #             l=m+1
        #         else:
        #             r=m-1
        #     return best            

        # ans=0        
        # for house in houses:
        #     ans=max(ans, closedistance(house))
        # return ans     

        # heaters.sort()
        # houses.sort()
        # ans=0
        # i=0
        # for h in houses:
        #     while i+1 < len(heaters) and abs(heaters[i+1]-h) <= abs(heaters[i]-h):
        #         i+=1
        #     ans=max(ans,abs(heaters[i]-h))    
        # return ans

        houses.sort()
        heaters.sort()
        heaters=[float('-inf')] + heaters + [float('inf')]
        pos=0
        ans=0
        for h in houses:
            while h >= heaters[pos]:
                pos+=1
            r=min( h-heaters[pos-1] , heaters[pos] -h)
            ans=max(ans,r)
        return ans    

        