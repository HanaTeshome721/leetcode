class Union:
    def __init__(self,n):
        self.root=list(range(n))
        self.rank=[0]*n
    def find(self,x):
        if x!=self.root[x]:
            self.root[x]=self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        rx=self.find(x)        
        ry=self.find(y) 
        if rx!=ry:
            if self.rank[rx]>self.rank[ry]:
                self.root[ry]=rx
            elif self.rank[rx]<self.rank[ry]:
                self.root[rx]=ry
            else:
                self.root[rx]=ry
                self.rank[ry]+=1               
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf=Union(n)
        res=[False] *len(queries) 
        edgeList.sort(key=lambda x:x[2])  
        queries= sorted([(p,q,lim,i) for i ,(p,q,lim) in enumerate(queries)], key=lambda x:x[2])
        i=0
        for p,q,lim,idx in queries:
            while i<len(edgeList) and edgeList[i][2]<lim:
                v,u,w=edgeList[i]
                uf.union(v,u)
                i+=1
            res[idx]=(uf.find(p)==uf.find(q))
        return res        

            