class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        pref=[0]*(len(nums)+1)
        for i in range(len(nums)):
            pref[i+1]=pref[i] + nums[i]
        return pref[1:]    