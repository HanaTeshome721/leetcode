class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        for i in range(l):
            for j in range(i,l):
                if nums[j]<nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]