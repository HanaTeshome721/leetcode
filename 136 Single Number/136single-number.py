class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        # p
        for num in nums:
            result ^= num
        return result
