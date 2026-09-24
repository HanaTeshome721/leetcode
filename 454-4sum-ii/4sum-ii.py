class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        d1=defaultdict(int)
        d2=defaultdict(int)
        l=len(nums1)
        cnt=0
        for i in range(l):
           for j in range(l):
                s=nums1[i] + nums2[j]
                if s not in d1:
                    d1[s]=1
                else:
                     d1[s]+=1           

        for i in range(l):
           for j in range(l):
                s=nums3[i] + nums4[j]
                if s not in d2:
                    d2[s]=1
                else:
                     d2[s]+=1
        for s1,n1 in d1.items():
          for s2,n2 in d2.items():
             if s1+s2==0:
                cnt+=n1*n2
               
        return cnt        
         