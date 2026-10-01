class Solution:
    def isHappy(self, n: int) -> bool:
        l=set()
        
        while n!=1:
            if n in l:
                return False
            l.add(n)    
            n=sum(int(i)**2 for i in str(n))
        return True        
           