class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        l=len(nums)
        # maxsum=float("-inf")
        # res=0
        # for i in range(l):
        #     cursum=nums[i]
        #     if cursum>maxsum:
        #         maxsum=cursum
        #     for j in range(i+1,l):
        #         cursum+=nums[j]
        #         if cursum>maxsum:
        #             maxsum=cursum
                    
        # return  maxsum      
        # pref=[0]*len(nums)
        # pref[0]=nums[0]
        # for i in range(1,l):
        #     pref[i]=nums[i] + pref[i-1]
        # return max(pref) 


        cursum=0
        res=nums[0]
        for i in range(len(nums)):
            
            if cursum<0:
                cursum=0
            cursum+=nums[i]    
            res=max(cursum,res)
        return res           

