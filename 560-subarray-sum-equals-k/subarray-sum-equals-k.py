class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt={}
        cm=0
        res=0
        for i in range(len(nums)):
            cm+=nums[i]
            if cm==k:
                res+=1
            if cm-k in cnt:
                res+=cnt[cm-k]    
            if cm in cnt:
                cnt[cm]+=1
            else:
                cnt[cm]=1
        return res        
