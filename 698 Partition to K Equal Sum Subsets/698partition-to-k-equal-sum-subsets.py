class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    #  target=sum(nums)/k
    #  used=[False]*len(nums)

    #  def backtrack(i,k,subsum):
    #     if k==0:
    #         return True
    #     if subsum==target:
    #        return backtrack(0,k-1,0)

    #     for j in range(i,len(nums)):
    #         if used[j] or subsum+nums[j]>target:
    #             continue
    #         used[j]=True
    #         if backtrack(j+1,k,subsum+ nums[j]):
    #             return True
    #         used[j]=False
    #     return False    
    #  return backtrack(0,k,0)                      



        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        n = len(nums)
        memo = {}

        def dfs(mask, curr_sum):
            if mask == (1 << n) - 1:
                return True

            if (mask, curr_sum) in memo:
                return memo[(mask, curr_sum)]

            for i in range(n):
                if not (mask & (1 << i)):
                    if curr_sum + nums[i] <= target:
                        new_mask = mask | (1 << i)

                        if dfs(new_mask, (curr_sum + nums[i]) % target):
                            return True

            memo[(mask, curr_sum)] = False
            return False

        return dfs(0, 0)



        # total = sum(nums)
        # if total % k != 0:
        #     return False

        # target = total // k
        # n = len(nums)
        # dp = [-1] * (1 << n)
        # dp[0] = 0

        # for mask in range(1 << n):
        #     if dp[mask] == -1:
        #         continue

        #     for i in range(n):
        #         if not (mask & (1 << i)):
        #             if dp[mask] + nums[i] <= target:
        #                 next_mask = mask | (1 << i)
        #                 dp[next_mask] = (dp[mask] + nums[i]) % target

        # return dp[(1 << n) - 1] == 0