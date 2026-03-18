class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
    #    op=0
    #    per=nums[-1]
    #    k=1
    #    for i in range(len(nums)-2,-1,-1):
    #         if nums[i]<=per:
    #             per=nums[i]
    #         else:
    #             k=math.ceil(nums[i]/per)
    #             op+=k-1
    #             per=nums[i]//k
    #    return op 

       pre=nums[-1]
       op=0
       for num in reversed(nums[:-1]):
            if num>pre:
                k=math.ceil(num/pre)
                op+=k-1
                pre=num//k
            else:
                pre=num
       return op             
