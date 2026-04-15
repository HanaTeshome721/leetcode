class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp={0:1}
        for t in range(1,target+1):
            dp[t]=0
            for n in nums:
                dp[t]+= dp.get(t-n,0)
        return dp[target]
        #  memo = {}

        # def dfs(t):
        #     if t == 0:
        #         return 1
        #     if t < 0:
        #         return 0
        #     if t in memo:
        #         return memo[t]

        #     res = 0
        #     for n in nums:
        #         res += dfs(t - n)

        #     memo[t] = res
        #     return res

        # return dfs(target)






