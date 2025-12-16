class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:      

        def rec(l,r):
            if l==r:
                return nums[l]
            pr=nums[r]-rec(l,r-1)
            pl=nums[l]-rec(l+1,r)
            return max(pr,pl)
        return rec(0,len(nums)-1)>=0        









        # arr=[0] *(n:=len(nums))
        # for i in range(n-1,-1,-1):
        #     arr[i] = nums[i]

        #     for j in range(i+1,n):
        #         arr[j] = max(nums[i] -arr[j],nums[j] - arr[j-1])

        # return arr[n-1] >= 0         
        
