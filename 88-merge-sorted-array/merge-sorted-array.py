class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=len(nums1)-1
        n-=1
        m-=1
        while n>-1 and m>-1:
            if nums1[m]>nums2[n]:
                nums1[l]=nums1[m]
                m-=1
            else:
                nums1[l]=nums2[n]
                n-=1
            l-=1    
        while n>-1:
            nums1[l]=nums2[n]
            n-=1
            l-=1




