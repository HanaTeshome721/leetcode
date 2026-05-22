class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py


class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        uf = UnionFind(n * n * 4)

        for r in range(n):
            for c in range(n):
                base = (r * n + c) * 4
                val = grid[r][c]
                
                if val == " ":
                    uf.union(base+0, base+1)
                    uf.union(base+1, base+2)
                    uf.union(base+2, base+3)
                elif val == "/":
                    uf.union(base+0, base+3)
                    uf.union(base+1, base+2)
                else: 
                    uf.union(base+0, base+1)
                    uf.union(base+2, base+3)

                if r + 1 < n:
                    uf.union(base+2, ((r+1)*n + c)*4 + 0)

                if c + 1 < n:
                    uf.union(base+1, (r*n + c+1)*4 + 3)

        return sum(1 for i in range(n*n*4) if uf.find(i) == i)