class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # curcost=0
        # l=0
        # res=0
        # for r in range(len(s)):
        #     curcost+=abs(ord(s[r])-ord(t[r]))
        #     while curcost>maxCost:
        #         curcost-=abs( ord(s[l])-ord(t[l]) )
        #         l+=1
        #     res=max(res,r-l+1)
        # return res    



        # l=0
        # cost=[abs(ord(a)-ord(b)) for a,b in zip(s,t)]
        # for r in range(len(s)):
        #     maxCost-=cost[r]
        #     if maxCost<0:
        #         maxCost+=cost[l]
        #         l+=1
        # return r-l+1

        l=0
        for r in range(len(s)):
            maxCost -= abs( ord(s[r]) - ord(t[r]))
            if maxCost<0:
                maxCost+=abs( ord(s[l])- ord(t[l]) )
                l+=1
        return r-l+1         







     