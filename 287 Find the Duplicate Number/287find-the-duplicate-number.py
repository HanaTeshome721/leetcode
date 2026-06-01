class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow=nums[0]
        # fast=nums[0]
        # while fast:
        #     slow=nums[slow]
        #     fast=nums[nums[fast]]
        #     if slow==fast:
        #         slow=nums[0]
        #         while slow!=fast:
        #             slow=nums[slow]
        #             fast=nums[fast]
        #         return slow  

        i=0
        
        while i<len(nums):
            ci=nums[i]-1
            if nums[i] != nums[ci]:
                nums[i] , nums[ci]= nums[ci] , nums[i]
            else:    
                i+=1
        return nums[-1]          
                         