class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # nums.sort()
        # ans=[]
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         ans.append(i)
        # return ans  

        nums.sort()
        l=0
        result=[]
        for r in range(len(nums)):
            if nums[l]==target:
                result.append(r)
            l+=1
            
        return result            

              