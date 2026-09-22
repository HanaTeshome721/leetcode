class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        ld=defaultdict(int)
        ps=set()
        for w,l in matches:
            ld[l]+=1
            ps.update([w,l])
        w=[]
        ol=[]
        for n in ps:
            if n not in ld:
                w.append(n)
            elif ld[n]==1:
                ol.append(n)
        w.sort()
        ol.sort()        
        return  [w,ol]            

