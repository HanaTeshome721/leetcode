class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        dp=set()
        dp.add(0)
        target=sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            nextset=set()
            for t in dp:
                if t+nums[i]==target:
                    return True
                nextset.add(t)
                nextset.add(t+nums[i])
            dp=nextset            
        return target in dp    