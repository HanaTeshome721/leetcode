class Solution:
    def countPrimes(self, n: int) -> int:
       if n<2:
         return 0
       isprime=[True for _ in range(n)] 
       isprime[0]=isprime[1]=False
       i=2
       while i*i<n:
            if isprime[i]:
                j=i*i
                while j<n:
                  isprime[j]=False
                  j+=i
            i+=1
       return sum(1 for i in range(n) if isprime[i] )           
                  
