class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum=0
        pref={0:1}
        res=0
        for n in nums:
            cursum+=n
            diff=cursum-k
            res+=pref.get(diff,0)
            pref[cursum]=1+pref.get(cursum,0)
        return res    








    #   d=defaultdict(int)
    #   d[0]=1
    #   c=0
    #   ans=0
    #   for n in nums:
    #     c+=n
    #     ans+=d[c-k]
    #     d[c]+=1    
    #   return ans 

    #  cnt=0
    #  persum=0
    #  perfi={0:1}

    #  for i in range(len(nums)):
    #     persum+=nums[i]
    #     removed=persum-k

    #     if removed in perfi:
    #         cnt+=perfi[removed]
    #     if persum in perfi:
    #         perfi[persum]+=1
    #     else:
    #         perfi[persum]=1
    #  return cnt               









        