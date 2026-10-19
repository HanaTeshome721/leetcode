class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        a=0
        b=0
        m=0
        i=len(piles)-1
        j=0
        while j<i:
            a+=piles[i]
            m+=piles[i-1]
            b+=piles[j]
            i-=2
            j+=1
        return m    
