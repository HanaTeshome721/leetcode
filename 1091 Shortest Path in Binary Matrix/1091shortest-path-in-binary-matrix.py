class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
       l=len(grid)
       if grid[0][0]:
        return -1
       q=deque()
       grid[0][0]=1
       q.append((0,0,1))
       d=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
       while q:
         for _ in range(len(q)):
            r,c,cnt=q.popleft()
            if (r,c)==(l-1,l-1):
                return cnt
            for dr,dc in d:
                nr=r+dr
                nc=c+dc
                if 0<=nr<l and 0<=nc<l and not grid[nr][nc]:
                    q.append((nr,nc,cnt+1))
                    grid[nr][nc]=1
       return -1 
                
