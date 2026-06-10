class Solution:
    def findGCD(self, nums: List[int]) -> int:
       mn=min(nums)
       mx=max(nums)
       def gcf(a,b):
         if b==0:
            return a
         return gcf(b,a%b)
       return gcf(mn, mx)          
# GCD(a, b) = GCD(b, a % b)




        # x = min(nums)
        # y = max(nums)
        # while x > 0:
        #     y, x = x, y % x
        # return y