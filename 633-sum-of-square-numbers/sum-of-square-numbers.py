class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n=int(math.sqrt(c))
        # print(n)
        if n*n==c:
            return True
        l=1
        r=n
        while l<=r:
            v=l*l +r*r
            print(v)
            if v==c:
                return True
            elif v>c:
                r-=1
            else:
                l+=1      
        return False      
