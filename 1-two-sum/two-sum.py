class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dc=defaultdict(int)
        for i,v in enumerate(nums):
            dc[v]=i

        for i,v in enumerate(nums):
            d=target-v
            if d in dc and dc[d]!=i:
                return [i,dc[d]]   