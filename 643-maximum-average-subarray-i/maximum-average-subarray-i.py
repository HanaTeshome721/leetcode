class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # if len(nums)==1:
        #     return nums[0]/k
        # mx=float('-inf')
        # for i in range(len(nums)-k+1):
        #     w=sum(nums[i:i+k])
        #     if w>mx:
        #         mx=w
        # return mx/k   
       
        w=sum(nums[:k])
        mx=max(float('-inf'),w)
        j=0
        for i in range(k,len(nums)):
            w=w -nums[j] + nums[i]
            j+=1  
            if w>mx:
                mx=w
        return mx/k         
