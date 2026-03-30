class Solution:
    def rob(self, nums: List[int]) -> int:
        # r1,r2=0,0

        # for n in nums:
        #     tem=max(r1+n,r2)
        #     r1=r2
        #     r2=tem
        # return r2    	
					
                  
				
				
				
			
        # if len(nums)==1: return nums[0]

        # nums[1] = max(nums[0], nums[1])

        # if len(nums)==2: return nums[1]

        # for i in range(2,len(nums)):
        #     nums[i] = max(nums[i-1],nums[i-2]+nums[i])

        # return nums[len(nums)-1] 

        memo={}

        def dfs(i):
            if i<0:
                return 0
            if i in memo:
                return memo[i]

            rob=nums[i] +dfs(i-2) 
            skip=dfs(i-1)
            memo[i]=max(rob,skip)
            return memo[i]
        return dfs(len(nums)-1)           






       