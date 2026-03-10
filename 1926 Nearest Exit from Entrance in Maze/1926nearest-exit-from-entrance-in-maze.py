class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row=len(maze)
        col=len(maze[0])
        maze[entrance[0]][entrance[1]]="+"
        q=deque()
        q.append([entrance[0],entrance[1],0])
        while q:
            r,c,dis=q.popleft()
            check=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for i,j in check:
                if 0<=i<row and 0<=j<col and maze[i][j]==".":
                    if i in [0,row-1] or j in [0,col-1]:
                        return dis+1
                    q.append((i,j,dis+1))
                    maze[i][j]="+"
        return -1                

















  
        # row , col=len(maze),len(maze[0])
        # q=deque([(entrance[0] , entrance[1],0)])
        # maze[entrance[0]][entrance[1]]="+"
        # while q:
        #     r,c,s=q.popleft()
        #     check=[(r+1,c),(r-1,c) , (r,c+1),(r,c-1)]
        #     for i ,j in check:
        #         if i>=0 and j>=0 and i<row and j <col and maze[i][j]==".":
        #             if i==0 or j==0 or i==row-1 or j==col-1:
        #                 return s+1
        #             q.append([i,j,s+1])
        #             maze[i][j]="+"
        # return -1       







