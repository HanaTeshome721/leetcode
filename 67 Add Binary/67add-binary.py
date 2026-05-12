class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # a=int(a,2)
        # b=int(b,2)
        # return bin(a+b)[2:]

        a1,b1=len(a)-1,len(b)-1
        carry=0
        res=[]
        while a1>=0 or b1>=0 or carry:
            da=int(a[a1]) if a1>=0 else 0
            db=int(b[b1]) if b1>=0 else 0

            total=da +db+carry
            carry=total//2
            res.append(str(total%2))
            a1-=1
            b1-=1
        return "".join(reversed(res))    