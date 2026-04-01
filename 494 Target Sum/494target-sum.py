class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memo={}
        # def backtrack(i,cus):
        #     if i==len(nums):
        #       return 1 if cus==target else 0
        #     if (i,cus) in memo:
        #         return memo[(i,cus)]   
        #     memo[(i,cus)]=(
        #         backtrack(i+1,cus + nums[i]) +
        #         backtrack(i+1,cus - nums[i])
        #     ) 
        #     return memo[(i,cus)]
        # return backtrack(0,0)       


        dp=defaultdict(int)
        dp[0]=1

        for i in range(len(nums)):
            nextdp=defaultdict(int)
            for curs,count in dp.items():
                nextdp[curs + nums[i]] +=count
                nextdp[curs - nums[i]] +=count
            dp=nextdp    
        return dp[target]    
