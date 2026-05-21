class Union:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])  
            x=self.parent[x]
        return self.parent[x]
    def union(self,x,y):
        rx,ry=self.find(x),self.find(y)
        if rx!=ry:
            if self.rank[x]>self.rank[y]:
                self.parent[ry]=rx  
            elif self.rank[y]>self.rank[x]:
                self.parent[rx]=ry
            else:
                self.parent[rx]=ry
                self.rank[ry]+=1 
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        uf=Union(n)
        row={}
        col={}

        for i, (x,y) in enumerate(stones):
            if x in row:
                uf.union(i,row[x])
            else:
                row[x]=i
            if y in col:
                uf.union(col[y],i)
            else:
                col[y]=i
        c=sum(1 for i in range(n) if i==uf.find(i)) 
        return n-c                   
