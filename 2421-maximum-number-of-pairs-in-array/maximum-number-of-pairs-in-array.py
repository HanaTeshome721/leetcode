class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        # pair=0
        # nopair=0
        # for i, n in enumerate(nums):
        #     if n in nums[i+1:]:
        #         pair+=1
        #         # idx=nums[i+1:].index(n)
        #         nums.remove(n)
        #         nums.remove(n)
        #         print(nums)
        #     else:
        #         nopair+=1
        # return [pair,nopair]  
        cnt=Counter(nums)
        p=0
        np=0
        for v,c in cnt.items():
            if c%2==0:
                p+=c//2
            else:
                p+=c//2
                np+=1  
        return [p,np]          