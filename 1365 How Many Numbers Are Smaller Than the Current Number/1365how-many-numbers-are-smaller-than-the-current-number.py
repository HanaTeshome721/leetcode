class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=sorted(nums)
        ans=[]
        for i in range(len(nums)):
            ans.append(s.index(nums[i]))
        return ans  