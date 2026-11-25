class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # cn=0
        # cursum=0
        
        # for i in range(len(nums)):
        #     if nums[i]%k==0:
        #         cn+=1
        #     cursum+=nums[i]
        #     if cursum%k==0:
        #         cn+=1
        # return cn 

      d=defaultdict(int)
      d[0]=1
      c=0
      ans=0
      for n in nums:
        c+=n

        if c%k in d:
            ans+=d[c%k]  
        d[c%k]+=1    
      return ans      
        # ans=0
        # for i in range(len(nums)):
        #   sb=nums[i]    
        #   if sb%k==0:
        #     ans+=1
        #   for j in range(i+1,len(nums)):
        #     sb+=nums[j]
        #     if sb%k==0:
        #         ans+=1
        # return ans  


        # cnt={}
        # cm=0
        # res=0
        # for i in range(len(nums)):
        #     cm+=nums[i]
        #     if cm%k==0:
        #         res+=1
        #     if cm//k in cnt:
        #         res+=cnt[cm//k]    
        #     if cm in cnt:
        #         cnt[cm]+=1
        #     else:
        #         cnt[cm]=1
        # return res  


        # cursum=0
        # pref={0:1}
        # res=0
        # for n in nums:
        #     cursum+=n
        #     diff=cursum%k
        #     res+=pref.get(diff,0)
        #     pref[diff]=1+pref.get(diff,0)
        # return res  