class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        change=False
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            elif change:
                return False
            elif i==0 or nums[i+1]>=nums[i-1]:
                nums[i]=nums[i+1]
            else:
                nums[i+1]=nums[i]
            change=True
        return True                    