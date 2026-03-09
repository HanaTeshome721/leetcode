class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
      q=deque()
      row=len(grid)
      col=len(grid[0])
      visit=set()  
      for r in range(row):
        for c in range(col):
            if grid[r][c]:
                q.append((r,c))
                
      res=-1         
      while q:
        r,c=q.popleft()
        res=grid[r][c]
        check=[(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
        for nr , nc in check:
            if 0<=nr<row and 0<=nc<col and grid[nr][nc]==0:
                grid[nr][nc]=grid[r][c] +1
                q.append((nr,nc))      
             
      return res-1 if res>1 else -1 





        # q = deque()
        # n = len(grid)

        # for r in range(n):
        #     for c in range(n):
        #         if grid[r][c] == 1:
        #             q.append((r,c))

        # if not q or len(q) == n*n:
        #     return -1

        # dist = -1

        # while q:
        #     dist += 1
        #     for _ in range(len(q)):
        #         r,c = q.popleft()

        #         for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        #             if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
        #                 grid[nr][nc] = 1
        #                 q.append((nr,nc))

        # return dist     






