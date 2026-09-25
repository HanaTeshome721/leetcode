class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        di={}
        for i,n in enumerate(nums):
            di[n]=i
        for n,o in operations:
            i=di[n]
            nums[i]=o
            di[o]=i
        return nums    