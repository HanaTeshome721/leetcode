class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return (bin(x^y).count('1'))
        ans=0
        xor=x^y
        while xor:
            ans+=1
            xor &=xor-1
        return ans    