class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
       ans=[]
       for i,n in enumerate(nums):
            j=0
            cn=0
            while j<len(nums):
               if i==j:
                    j+=1
                    continue
               elif nums[j]<nums[i]:
                    cn+=1  
               j+=1         
            ans.append(cn)
       return ans             