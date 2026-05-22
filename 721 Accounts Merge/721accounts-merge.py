class Union:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n
    def find(self,n):
        if n!=self.parent[n]:
            self.parent[n]=self.find(self.parent[n])
        return self.parent[n]
    def union(self,x,y):
        rx,ry=self.find(x),self.find(y)
        if rx!=ry:
            if self.rank[rx]>self.rank[ry]:
                self.parent[ry]=rx
            elif self.rank[ry]>self.rank[rx]:
                self.parent[rx]=ry
            else:
                self.parent[rx]=ry
                self.rank[ry]+=1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        uf=Union(n)
        emailtoacc={}
        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e in emailtoacc:
                    uf.union(i,emailtoacc[e])
                else:
                    emailtoacc[e]=i
        emailgroup=defaultdict(list)      
        for e,i in emailtoacc.items():
            led=uf.find(i)
            emailgroup[led].append(e)
        res=[]
        for r,e in emailgroup.items():
            name=accounts[r][0]             
            res.append([name]+ sorted(e))
        return res    