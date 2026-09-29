class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
       num=set(nums)
       longest=0 
      
       for n in num:
         if n-1 not in num:
            lenght=0
            while n+lenght in num:
                lenght+=1
            longest=max(longest,lenght)          
       return longest     