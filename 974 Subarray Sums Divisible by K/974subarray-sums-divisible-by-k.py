class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
    #    pefs=0
    #    remaind=defaultdict(int)
    #    remaind[0]=1
    #    cnt=0
    #    for n in nums:
    #         pefs+=n
    #         rem=pefs%k
    #         cnt+=remaind[rem]
    #         remaind[rem]+=1
      
    #    return cnt 


      
    #   mode=[0]*k
    #   mode[0]=1
    #   pefi=0
    #   cnt=0
    #   for n in nums:
    #     pefi+=n
    #     m = (pefi %k+k) %k
    #     cnt+=mode[m]
    #     mode[m]+=1
    #   return cnt 


      frq=[0]*k
      frq[0]=1
      cnt=0
      perfi=0

      for n in nums:
        perfi+=n
        m=perfi%k
        if frq[m]>0:
            cnt+=frq[m]
        frq[m]+=1
      return cnt       