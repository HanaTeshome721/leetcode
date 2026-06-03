class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # m=len(nums)
        # for i in range(m+1):
        #     if i not in nums:
        #         return i

        # res=len(nums)
        # for i in range(len(nums)):
        #     res+=(i-nums[i])
        # return res    

        # n = len(nums)
        # expected = n * (n + 1) // 2
        # actual = sum(nums)
        # return expected - actual


    
        i=0
        while i <len(nums):
            ci=nums[i]
            if nums[i]< len(nums) and nums[i]!=nums[ci]:
                nums[i],nums[ci]=nums[ci],nums[i]
            else:
                i+=1
             
        for i in range(len(nums)):
            if i!=nums[i]:
                return i                            
        return len(nums)
        # n=len(nums)
        # xor=n
        # for i in range(n):
        #     xor^=i^nums[i]
        # return xor    