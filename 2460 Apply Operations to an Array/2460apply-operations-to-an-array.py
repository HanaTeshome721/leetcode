class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
      for i in range(len(nums)-1):
        if  nums[i]==nums[i+1]:
            nums[i]*=2
            nums[i+1]=0
      nozero=0
      for i,v in enumerate(nums):
        if v>0:
            nums[nozero],nums[i]=nums[i],nums[nozero]
            nozero+=1
      return nums      
