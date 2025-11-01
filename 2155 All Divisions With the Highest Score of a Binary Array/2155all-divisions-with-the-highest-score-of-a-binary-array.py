class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # total=hight=curs=sum(nums)
        # ans=[0]
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         curs+=1
        #     else:
        #         curs-=1
        #     if curs==hight:
        #         ans.append(i+1)    
        #     elif curs>hight:
        #         hight=curs
        #         ans=[i+1] 
        # return ans              

        total=right=sum(nums)
        left=0
        ans=[]
        maxi=-1
        for i in range(len(nums)+1):
            score=right+left
            if score>maxi:
                maxi=score
                ans=[i]
            elif score==maxi:
                ans.append(i)
            if i <len(nums):
               if nums[i] ==1:
                  right-=1
               else:
                left+=1
        return ans           


