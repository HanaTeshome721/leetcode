class Union:
    def __init__(self,n):
        self.root=[i for i in range(n)]
        self.rank=[0]*n

    def find(self,x):
        if x==self.root[x]:
            return x
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        com=n
        uni=Union(n)

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] and uni.find(i) != uni.find(j):
                    com-=1
                    uni.union(i,j)
        return com            
        