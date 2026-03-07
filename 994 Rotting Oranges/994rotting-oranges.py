class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      q=deque()
      row=len(grid)
      col=len(grid[0])
      fresh,time=0,0  
      for r in range(row):
        for c in range(col):
            if grid[r][c]==2:
                q.append((r,c))
            if grid[r][c]==1:
                fresh+=1    
      d=[(1,0),(-1,0),(0,1),(0,-1)]
      while q and fresh>0:
        for _ in range(len(q)):
           r,c=q.popleft()
           for dr,dc in d:
             nr=r+dr
             nc=c+dc
             if (nr<0 or nc<0 or nr>=row or nc>=col or grid[nr][nc]!=1):
                continue
             grid[nr][nc]=2
             q.append((nr,nc))
             fresh-=1
        time+=1
      return time if fresh==0 else -1          
        
