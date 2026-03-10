class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
         l=len(board)
         board.reverse()
         def intpos(squer):
            r=(squer-1) //l
            c=(squer-1)%l
            if r%2:
                c=l-1-c
            return [r,c]       
         q=deque()
         q.append((1,0))
         visit=set()
         while q:
            squer,move=q.popleft()
            for i in range(1,7):
                nextsquer=squer+i
                r,c=intpos(nextsquer)
                if board[r][c]!=-1:
                    nextsquer=board[r][c]
                if nextsquer==l*l:
                    return move +1
                if nextsquer not in visit:    
                    q.append((nextsquer,move+1))
                    visit.add(nextsquer)                        
         return -1










