class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=defaultdict(int)
        for i ,v in enumerate(nums):
            dif=target-v
            if dif in dic:
                return [dic[dif],i]
            else:
                dic[v]=i    
  