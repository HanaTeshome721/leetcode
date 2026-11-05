class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        mn=float('inf')
        l=0
        w=0
        for r in range(len(nums)):
             w+=nums[r]
             while w>=target:
                mn=min(r-l+1,mn)
                w-=nums[l]
                l+=1
             
        return 0 if mn==float("inf") else mn