class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # se=set(nums)
        # mal=0
        # for i in set(nums):
        #     if i-1 not in se:
        #         le=0
        #         while i+le in se:
        #             le+=1
        #             mal=max(le,mal)
        # return mal            
        if len(nums)==0:
            return 0
        s=set(nums)   
        longest=0
        for i in s:
            if i-1 in s:
                continue
            le=1
            st=i+1
            while st in s:
                le+=1
                st+=1
            longest=max(le,longest)    
        return longest        


