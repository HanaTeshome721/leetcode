class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # i=0
        # while i<len(nums):
        #     ci=nums[i]-1
        #     if nums[i]!=nums[ci]:
        #         nums[i],nums[ci]=nums[ci],nums[i]
        #     else:
        #         i+=1    
        # ans=[]
        # for i in range(1,len(nums)+1):
        #     if i!=nums[i-1]:
        #         ans.append(i)
        # return  ans       



        n = len(nums)+1
        seen = [False]*n
        for i in nums:
            seen[i] = True
        return [i for i in range(1,n) if not seen[i]]