class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
       ans=[]
       for i,n in enumerate(nums):
            j=0
            cn=0
            while j<len(nums):
                if nums[j]<nums[i]:
                    cn+=1  
                j+=1         
            ans.append(cn)
       return ans             


        # s=sorted(nums)
        # ans=[]
        # for i in range(len(nums)):
        #     ans.append(s.index(nums[i]))
        # return ans  

        # temp=sorted(nums)
        # has={}
        # res=[]

        # for i in range(len(temp)):
        #     if temp[i] not in has:
        #         has[temp[i]]=i

        # for i in nums:
        #     res.append(has[i])
        # return res            

