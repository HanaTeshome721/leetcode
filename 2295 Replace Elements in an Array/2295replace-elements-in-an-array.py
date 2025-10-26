class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # has={}
        # for i,v in enumerate(nums):
        #     has[v]=i
        # for v,n in operations:
        #     index=has[v]
        #     nums[index]=n
        #     has[n]=index
        #     del has[v]
        # return nums  
        
        # swap={}
        # for i,v in reversed(operations):
        #     swap[i]=swap[v] if v in swap else v
        # for i,v in enumerate(nums):
        #     if v in swap:
        #         nums[i]=swap[v]
        # return nums            





        swap={}
        for i,n in reversed(operations):
            swap[i]=swap[n] if n in swap else n
        for i,v  in enumerate(nums):
            if v in swap:
                 nums[i]=swap[v] 
        return nums

        # seen={}
        # for i,v in enumerate(nums):
        #     seen[v]=i
        # for i,n in operations:
        #     i=seen.pop(i)
        #     nums[i]=n
        #     seen[n]=i
        # return nums         