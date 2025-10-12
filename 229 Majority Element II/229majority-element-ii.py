class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
      ans=[]
      hash=defaultdict(int)
      for i in nums:
        if i in hash:
           hash[i]+=1
        else:
            hash[i]=1     
      for i,v in hash.items():
          if v>len(nums)//3 :
             ans.append(i)
      return ans 
# TLE
    #   ans=[]
    #   n=len(nums)
    #   thre=n//3
    #   for i in set(nums):
    #     if nums.count(i) >thre:
    #         ans.append(i)
    #   return ans        
      