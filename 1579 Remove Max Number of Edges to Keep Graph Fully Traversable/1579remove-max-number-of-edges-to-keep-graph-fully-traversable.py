class Union:
    def __init__(self,n):
        self.n=n
        self.root=[i for i in range(n+1)]
        self.rank=[1]*(n+1)
    def find(self,x):
        while x != self.root[x]:
            self.root[x]=self.root[self.root[x]]
            x=self.root[x]
        return self.root[x]   
    def union(self,x,y):
        rx=self.find(x)
        ry=self.find(y)
        if rx==ry:
            return 0
        if self.rank[rx]>self.rank[ry]:
            self.root[ry]=rx         
        elif self.rank[rx]<self.rank[ry]:
            self.root[rx]=ry
        else:
            self.root[rx]=ry 
            self.rank[ry] +=1
        self.n-=1
        return 1
    def connected(self):
        return self.n==1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alic,bob=Union(n) ,Union(n)
        cnt=0
        for t,s,d in edges:
            if t==3:
                cnt+=alic.union(s,d) | bob.union(s,d)
        for t,s,d in edges:
            if t==1:
                cnt+=alic.union(s,d)  
            elif t==2:
                cnt+=bob.union(s,d)
        if alic.connected() and bob.connected():
            return len(edges)-cnt
        return -1    
