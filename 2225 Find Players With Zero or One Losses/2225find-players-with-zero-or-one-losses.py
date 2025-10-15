class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # zerol=set()
        # onel=set()
        # morel=set()
        # for w,l in matches:
        #     if l in onel:
        #         morel.add(l)
        #     else:
        #         onel.add(l) 
        #     zerol.add(w)
        # return[sorted(zerol-onel),sorted(onel-morel)]   
        zer=[]
        on=[]
        has=defaultdict(int)

        for w,l in matches:
            has[l]+=1
              
            has[w]  
        for i,v in has.items():
            if v==0:
                zer.append(i)
            elif v==1:
                on.append(i)
        zer.sort()
        on.sort()        
        return [zer,on]                 
