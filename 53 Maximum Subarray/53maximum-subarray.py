class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      mx=nums[0]
      curs=0
      for n in nums:
         if curs<0:
            curs=0
         curs+=n
         if curs>mx:
            mx=curs
      return mx         