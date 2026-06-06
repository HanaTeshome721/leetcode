class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            ci=nums[i]-1
            if nums[i]!=nums[ci]:
                nums[i],nums[ci]=nums[ci],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                miss=i+1
                dup=nums[i]
                return [dup,miss]            
    