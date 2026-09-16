class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums + nums
        ans=[]
        for i in range(2*(len(nums))):
            ans.append(nums[i%len(nums)])
        return ans    