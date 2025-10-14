class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # changed=False
        # for i in range(len(nums)-1):
        #     if nums[i]<=nums[i+1]:
        #         continue
        #     if changed:
        #         return False
        #     if i==0 or nums[i-1]<=nums[i+1]:
        #         nums[i]=nums[i+1]
        #     else:
        #         nums[i+1]=nums[i]
        #     changed=True
        # return True                    

        # i=0
        # k=1
        # n=len(nums)
        # while i<n-1:
        #     if nums[i]>nums[i+1]:
        #         if not k: return False
        #         k-=1
        #         if i>0 and nums[i-1]>nums[i+1]:
        #             nums[i+1]=nums[i]
        #     i+=1
        # return True      

        count=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
                if count>1:
                    return False
                if i ==0:
                    nums[i]=nums[i+1]
                if nums[i-1]>nums[i+1]:
                    nums[i+1]=nums[i]
                else:
                    nums[i]=nums[i+1]
        return True                              
      