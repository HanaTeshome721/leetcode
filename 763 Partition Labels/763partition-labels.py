class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # lastindex={}
        # for i,c in enumerate(s):
        #     lastindex[c]=i
        # res=[]
        # size=end=0

        # for i,c in enumerate(s):
        #     size+=1
        #     end=max(end,lastindex[c])
        #     if i==end:
        #         res.append(size)
        #         size=0
        # return res 



        count={}
        for i,v in enumerate(s):
            count[v]=i
        res=[]
        cur=set()
        l=0
        for r ,c in enumerate(s):
            cur.add(c)
            if count[c]==r:
                cur.remove(c)
                if not cur:
                    res.append(r-l+1)
                    l=r+1
        return res            








    

        