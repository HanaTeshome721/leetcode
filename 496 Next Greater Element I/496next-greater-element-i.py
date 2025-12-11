class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # d=defaultdict(lambda:-1)
        # s=[]
        # for n in  nums2:
        #     while s and s[-1]<n:
        #         d[s.pop()]=n
        #     s.append(n)    
        # return [d[n] for n in nums1] 

        d={n:i for i,n in enumerate(nums1)}
        ans=[-1]*len(nums1)
        stack=[]
        for n in nums2:
           while  stack and stack[-1]<n:
              ind=d[stack.pop()]
              ans[ind]=n
           if n in nums1:
             stack.append(n)
        return ans           
