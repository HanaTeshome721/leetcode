class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
       xor=0
       for n in nums:
         xor^=n
      
       diffbit=xor & -xor
    #    diffbit=1
    #    while not (diffbit &xor):
    #         diffbit=diffbit <<1
       a,b=0,0     
       for n in nums:
        if diffbit&n:
            a^=n
        else:
            b^=n
       return [a,b]             