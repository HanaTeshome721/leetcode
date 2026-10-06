class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        l=len(nums)
        cn=0
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]==nums[j] and (i*j)%k==0:
                    cn+=1 
        return cn            