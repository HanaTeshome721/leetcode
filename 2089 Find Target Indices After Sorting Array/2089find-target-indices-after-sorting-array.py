class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        # ans=[]
        # for i,v in enumerate(nums):
        #     if v==target:
        #         ans.append(i)
        # return ans   

        # nums.sort()
        # l=0
        # result=[]
        # for r in range(len(nums)):
        #     if nums[r]==target:
        #         result.append(r)
        #         l+=1
        #     else:
        #         l+=1
        # return result  
        nums.sort()
        return [i for i,v in enumerate(nums) if v ==target]          


     