class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
       mincosts=[] 
       for ca,cb in costs:
         mincosts.append([cb-ca,ca,cb])
       mincosts.sort(key=lambda p:p[0])
       res=0
       for i in range(len(mincosts)):
         if i<len(mincosts)/2:
            res+=mincosts[i][2]
         else:
            res+=mincosts[i][1]
       return res        


