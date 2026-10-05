class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
       f=[i for i in range(1,n+1)]
       i=0
       while len(f)>1:
         i=(i+k-1)%len(f)
         f.pop(i)
         
       return f[0]  
      

