class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #    if len(p)>len(s):
        #     return []
        #    countp={}
        #    countw={} 
        #    for i in range(len(p)):
        #      countp[p[i]]=1+countp.get(p[i],0)
        #      countw[s[i]]=1+countw.get(s[i],0)
        #    res=[0] if countw==countp else []
        #    l=0 
        #    for i in range(len(p),len(s)):
        #         countw[s[i]]=1+countw.get(s[i],0)
        #         countw[s[l]]-=1
            
        #         if countw[s[l]]==0:
        #             countw.pop(s[l])
        #         l+=1
                
        #         if countw==countp:
        #             res.append(l)
        #    return res        


        # if len(p)>len(s):
        #     return []
        # count={}
        # countw={}

        # for i in range(len(p)):
        #     count[p[i]]=1+count.get(p[i],0)
        #     countw[s[i]]=1+countw.get(s[i],0)
        # res=[]
        # if count==countw:
        #     res.append(0)  
        # for i in range(len(p),len(s)):
        #     countw[s[i]]=1+countw.get(s[i],0)
        #     countw[s[i-len(p)]]-=1
        #     if countw[s[i-len(p)]]==0:
        #         del countw[s[i-len(p)]]
            
        #     if countw==count:
        #         res.append(i-len(p)+1)
        # return res    





        # LS, LP, S, P, A = len(s), len(p), 0, 0, []
        # if LP > LS: 
        #     return []
        # for i in range(LP): S, P = S + hash(s[i]), P + hash(p[i])
        # if S == P: A.append(0)
        # for i in range(LP, LS):
        #     S += hash(s[i]) - hash(s[i-LP])
        #     if S == P: A.append(i-LP+1)
        # return A 
        if len(p)>len(s):
            return []
        n=len(p)
        m=len(s)
        countp=Counter(p)
        countw=Counter(s[:n])
        res =[0] if countp==countw else []
        for i in range(n,m):
            lc=s[i-n]
            rc=s[i]
                
            countw[lc]-=1
          
            if countw[lc]==0:
                del countw[lc]
            
            countw[rc]+=1
            if countw==countp:
                res.append(i-n+1)
        return res        







        

        