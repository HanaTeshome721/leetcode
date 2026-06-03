class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # cnt=Counter(nums)
        # ans=[]
        # for i,v in cnt.items():
        #     if v>1:
        #         ans.append(i)
        # return ans 
        # p=[0]*(len(nums)+1)
        # ans=[]
        # for v in nums:
        #     if p[v]:
        #         ans.append(v)
        #     else:
        #         p[v]=1
        # return ans            

        i=0
        res=set()
        while i<len(nums):
            ci=nums[i]-1
            if nums[i]!=nums[ci]:
                nums[i],nums[ci]=nums[ci],nums[i]
            else:
                if i!=ci:
                    res.add(nums[i])
                i+=1
        return list(res)                
                




        # se=set()
        # du=set()
        # for i in nums:
        #     if i in se:
        #         du.add(i)
        #     else:
        #         se.add(i)
        # return list(du)                   