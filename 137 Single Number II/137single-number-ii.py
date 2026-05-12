class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      one=0
      two=0
      for n in nums:
        one=(one^n)& ~two
        two=(two ^n) & ~one
      return one  