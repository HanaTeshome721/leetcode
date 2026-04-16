class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

           prevrow=[poured]
           for row in range(1,query_row+1):
                currow=[0]*(row+1)
                for i in range(row):
                    extra=prevrow[i]-1
                    if extra>0:
                        currow[i]+=extra*0.5 
                        currow[i+1]+=extra*0.5
                prevrow=currow
           return min(1,prevrow[query_glass])              



