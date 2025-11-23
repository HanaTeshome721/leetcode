class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for n in nums1:
            if n in nums2:
                ans.append(n)
        ans=list(set(ans) )       
        return ans         