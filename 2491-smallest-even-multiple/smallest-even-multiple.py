class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if not n%2 :
            return n
        return n*2    