class Solution:
    def isHappy(self, n: int) -> bool:
    #     v=set()
    #     while n!=1 and n not in v:
    #         v.add(n)
    #         n=self.sqs(n)
    #         if n in v:
    #             return False
    #     return True
    # def sqs(self,n:int) -> int:
    #     out=0
    #     while n:
    #         d=n%10
    #         out+=d**2
    #         n=n//10
    #     return out   

        v=set()
        while n not in v:
            v.add(n)
            n=sum([int(i)**2 for i in str(n)])
        return n==1                 