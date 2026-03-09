class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q=deque()
        row=len(isWater)
        col=len(isWater[0])
        for r in range(row):
            for c in range(col):
                if isWater[r][c]:
                    isWater[r][c]=0
                    q.append((r,c))
                else:
                    isWater[r][c]=-1

                    
        while q:
            r,c=q.popleft()    
            check=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in check:
                if 0<=nr<row and 0<=nc<col and isWater[nr][nc]==-1:
                    isWater[nr][nc]=isWater[r][c] +1
                    q.append((nr,nc))
        return isWater                    
