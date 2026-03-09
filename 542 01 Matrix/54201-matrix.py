class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        row=len(mat)
        col=len(mat[0])
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=float("inf")
        while q:
            r,c=q.popleft() 
            check=[(r+1,c), (r-1,c) ,(r,c+1),(r,c-1)]
            for nr, nc in check:
                if 0<=nr<row and 0<=nc<col and mat[nr][nc]>mat[r][c]:
                    mat[nr][nc]=mat[r][c]+1
                    q.append((nr,nc))
        return mat                              
        