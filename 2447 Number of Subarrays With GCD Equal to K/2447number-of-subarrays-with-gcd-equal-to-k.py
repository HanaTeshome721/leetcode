class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            cug=0
            for j in range(i,n):
                cug=gcd(cug,nums[j])
                if cug==k:
                    ans+=1
                elif cug<k:
                    break
        return ans                
