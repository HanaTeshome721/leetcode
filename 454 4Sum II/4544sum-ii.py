class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
       has=defaultdict(int)
       ans=0

    #    for n1 in nums1:
    #     for n2 in nums2:
    #         has[n1+n2]+=1
    #    for n3 in nums3:
    #     for n4 in nums4:
    #         ans+=has[-(n3+n4)]
    #    return ans  

    #    count=Counter(a+b for a in nums1 for b in nums2)
    #    return sum(count[-(c+d)] for c in nums3 for d in nums4)   
    #    c1,c2,c3,c4=Counter(nums1),Counter(nums2),Counter(nums3),Counter(nums4)
    #    a1=Counter()
    #    ans=0
    #    for k1,v1 in c1.items():
    #     for k2,v2 in c2.items():
    #         a1[k1+k2]+=v1*v2
    #    for k3,v3 in c3.items():
    #     for k4, v4 in c4.items():
    #         ans+=a1[-k3-k4]*v3*v4
    #    return ans   

       m={}
       for a in nums1:
        for b in nums2:
            q=a+b
            if q in m:
                m[q]+=1
            else:
                m[q]=1
       ans=0
       for c in nums3:
        for d in nums4:
            x=c+d
            y=-1*x
            if y in m:
                ans+=m[y]
           
       return ans                             