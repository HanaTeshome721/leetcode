class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # cunt=Counter(nums)
        # p,l=0,0
        # for i,v in cunt.items():
        #     p=p+v//2
        #     l=l+v%2
        # return [p,l] 
      ferq=Counter(nums)     
      pair=sum([fe//2 for fe in ferq.values() ]) 
      lov=len(nums)-pair*2
      return [pair,lov]            
