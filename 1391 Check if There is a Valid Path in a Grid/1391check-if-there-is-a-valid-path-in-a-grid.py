class Unionfind:
    def __init__(self,size):
        self.root=[i for i in range(size)]

    def find(self,x):
        if x== self.root[x]:
            return x
        self.root[x]=self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        rx=self.find(x)
        ry=self.find(y)
        if rx != ry:
            self.root[rx]=ry
class Solution:
    def hasValidPath(self, grid):   
        n=len(grid)
        m=len(grid[0])
        dsj=Unionfind(n*m)

        dirc={
            1:[(0,-1),(0,1)],
            2:[(-1,0),(1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(0,1),(-1,0)]
        }                 

        for r in range(n):
            for c in range(m):
                for dr,dc in dirc[grid[r][c]]:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr <n and 0<=nc<m:
                       if (-dr,-dc) in dirc[grid[nr][nc]]:
                         id1=r*m+c
                         id2=nr*m+nc
                         dsj.union(id1,id2)
        return dsj.find(0)==dsj.find(n*m-1)                 