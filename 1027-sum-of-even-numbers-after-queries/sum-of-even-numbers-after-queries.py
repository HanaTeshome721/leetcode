class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        an=[]
        s=[n for n in nums if n%2==0]
        se=sum(s)
        for v,i in queries:
            if (v%2 and nums[i]%2):
                nums[i]+=v
                se+=nums[i]
            elif (v%2==0 and nums[i]%2==0):
                nums[i]+=v
                se+=v
            elif nums[i]%2==0:
                se-=nums[i]
                nums[i]+=v 
            else:
                nums[i]+=v

            an.append(se)    
        return an   