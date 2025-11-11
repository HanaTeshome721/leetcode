class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    #   w=sum(nums[:k])
    #   mx=w
    #   l=0
    #   for i in range(k,len(nums)):
    #     w=w-nums[l] +nums[i]
    #     mx=max(w,mx)
    #     l+=1
    #   return mx/k 
      w=sum(nums[:k])
      mx=w/k
      for i in range(k,len(nums)):
        w=w+(nums[i] -nums[i-k])
        mx=max(w/k,mx)
      return mx  



   
    