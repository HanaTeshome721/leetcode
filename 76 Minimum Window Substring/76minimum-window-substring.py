class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #   if t=='':return ''
        #   countT,window={},{}  
        #   for c in t:
        #     countT[c]=1+countT.get(c,0)

        #   have,need=0,len(countT)  
        #   res=[-1,-1]
        #   reslen=float('inf')  
        #   l=0 

        #   for r in range(len(s)):
        #     c=s[r]
        #     window[c]=1+window.get(c,0)

        #     if c in countT and window[c]==countT[c]:
        #         have+=1
        #     while have == need:
        #         if r-l+1 <reslen:
        #             reslen=r-l+1 
        #             res=[l,r]

        #         rc=s[l]
        #         window[rc]-=1
        #         if rc in countT and window[rc] <countT[rc]:
        #             have-=1
        #         l+=1
        #   l,r=res
        #   return s[l:r+1] if reslen!=float('inf') else ''    

            need=Counter(t)
            missing=len(t)
            minlen=float('inf')
            st,e,l=0,0,0

            for r,c in enumerate(s):
                if need[c]>0:
                    missing-=1
                need[c]-=1

                while missing==0:
                    if r-l <minlen:
                        minlen=r-l
                        st,e=l,r

                    need[s[l]]+=1
                    if need[s[l]]>0:
                        missing+=1
                    l+=1
            return '' if minlen==float('inf') else s[st:e+1]                








          