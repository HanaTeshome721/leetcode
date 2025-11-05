class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums.sort()
        # ans=[]
        # if len(nums)<3:
        #     return nums[-1]
        # has=Counter(nums)
        # for i in has:
        #     ans.append(i)  
        # return  ans[-1] if len(ans)<3 else ans[-3] 


        # nums.sort()
        # if len(nums)<3:
        #     return nums[-1]
        # elif len(nums)>len(set(nums)):
        #     dic=defaultdict(int)
        #     ans=[]
        #     for i in nums:
        #         if i in dic:
        #             continue
        #         else:
        #             dic[i]=1
        #     for i in dic:
        #         ans.append(i)
        #     if len(ans)<3:
        #         return ans[-1]
        #     else:
        #         return ans[-3]
        # else:
        #     return nums[-3]    



        # nums=set(nums)
        # nums=list(nums)
        # nums.sort()
        # if len(nums)>=3:
        #     return nums[-3]
        # else:
        #     return nums[-1]


        # nums=sorted(set(nums),reverse=True) 
        # if len(nums)>=3:
        #     return nums[2]
        # else:
        #    return  nums[0]    

       nums.sort(reverse=True) 
       per=nums[0]
       cn=1
       for i in range(len(nums)):
         if nums[i]!=per:
            cn+=1
            per=nums[i]
         if cn==3:
            return per
       return nums[0]                  
        

        

