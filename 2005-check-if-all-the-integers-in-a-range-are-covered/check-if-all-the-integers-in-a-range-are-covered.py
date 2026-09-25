class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        l=set()
        for i,v in ranges:
             for n in range(i,v+1):
                l.add(n)
        for i in range(left,right+1):
            if i not in l:
                return False
        return True                   

