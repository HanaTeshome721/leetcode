class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        d=num//3
        n1=d-1
        n2=d
        n3=d+1

        if n1+n2+n3==num:
            return [n1,n2,n3]
        return []