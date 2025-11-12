class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # if sum(nums)<target:
        #     return 0
        # l=0
        # w=0
        # ans=float('inf')
        # for i in range(len(nums)):
        #     w+=nums[i]
        #     while 1:
        #         if w>=target:
        #             ans=min(ans,i-l+1)
        #             w-=nums[l]
        #             l+=1
        #         else:
        #             break
        # return ans   
        # ans=float('inf')
        # l=0
        # w=0
        # for i in range(len(nums)):
        #     w+=nums[i]
        #     while w>=target:
        #         ans=min(ans,i-l+1)
        #         w-=nums[l]
        #         l+=1
        # return 0 if ans==float('inf') else ans  
    #    l=0
    #    r=0
    #    s=nums[0]
    #    ans=float('inf')
    #    n=len(nums) 
    #    while l<n and r<n:
    #         if s<target:
    #             r+=1
    #             if r<n:
    #                 s+=nums[r] 
    #         else:
    #             ans=min(ans,r-l+1)
    #             s-=nums[l]
    #             l+=1
    #    if ans==float('inf'):
    #         return 0
    #    else:
    #         return ans 
            l,res=0,len(nums)+1
            for r in range(len(nums)):
                target-=nums[r]
                while target<=0:
                    res=min(res,r-l+1)
                    target+=nums[l]
                    l+=1
            return res % (len(nums)+1)        

                    







         
