class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r=[0]*len(nums)
        r[0]=nums[0]
        for i in range(1,len(nums)):
            r[i]=nums[i]+ r[i-1]
        return r 

        # for i in range(1,len(nums)):
        #     nums[i]+=nums[i-1]
        # return nums    

        # s=0
        # r=[]
        # for i in range(len(nums)):
        #     s+=nums[i]
        #     r.append(s)
        # return r   

        # res=[nums[0]]
        # for i in range(1,len(nums)):
        #     res.append(nums[i]+res[i-1])
        # return res    





