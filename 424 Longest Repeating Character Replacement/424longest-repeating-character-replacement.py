class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    #    count={}
    #    l=0
    #    maxf=0
    #    ans=0
    #    for r in range(len(s)):
    #         count[s[r]]=1+count.get(s[r],0)
    #         maxf=max(maxf,count[s[r]])
    #         while (r-l+1) -maxf >k:
    #             count[s[l]]-=1
    #             l+=1
    #         ans=max(ans,r-l+1)
    #    return ans 

    #    d={}
    #    c=0
    #    m=0
    #    l=0
    #    for i in s:
    #      if i in d:
    #         d[i]+=1
    #      else:
    #         d[i]=1


    #      if m<d[i]:
    #         m=d[i]
    #      elif c<k:
    #         c+=1
    #      else:
    #         d[s[l]]-=1
    #         l+=1
    #    return m+c     
        l=0
        res=0
        frq=defaultdict(int)
        maxf=0
        for r in range(len(s)):
            frq[s[r]]+=1
            maxf=max(maxf,frq[s[r]])
            while r-l+1 -maxf >k:
                frq[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res        






