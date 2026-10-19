class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        snum=list(set(nums))
        
        snum.sort()
        if len(snum)<3:
            return snum[-1]
        else:
            return snum[-3]    
