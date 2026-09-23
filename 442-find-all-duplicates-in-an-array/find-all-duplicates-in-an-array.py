class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans=[]
        # for i,n in enumerate(nums):
        #     if i<len(nums)-1 and n in nums[i+1:]:
        #         ans.append(n) 
        # return ans        
        cnt=Counter(nums)
        for i,n in cnt.items():
            if n==2:
                ans.append(i)
        return ans        