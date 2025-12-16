class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    #   left=self.bin(nums,target,True)
    #   right=self.bin(nums,target,False)
    #   return [left,right]

    # def bin(self,nums,target,leftbise):
    #      l=0
    #      r=len(nums)-1
    #      i=-1
    #      while l<=r:
    #         m=(l+r)//2
    #         if target>nums[m]:
    #             l=m+1
    #         elif target<nums[m]:
    #             r=m-1
    #         else:
    #             i=m  
    #             if leftbise:
    #                 r=m-1
    #             else:
    #                 l=m+1
    #      return i  




    #    ans=[-1,-1]
    #    l=0
    #    r=len(nums)-1
    #    while l<=r:
    #         m=(l+r)//2
    #         if target==nums[m]:
    #             ans[0]=m
    #             r=m-1
    #         elif target>nums[m]:
    #             l=m+1
    #         else:
    #             r=m-1

    #    l,r=0,len(nums)-1
    #    while l<=r:
    #         m=(r+l)//2
    #         if target==nums[m]:
    #             ans[1]=m
    #             l=m+1
    #         elif target>nums[m]:
    #             l=m+1
    #         else:
    #             r=m-1
    #    return ans         

        out=[-1,-1]
        l=0
        r=len(nums)-1

        while l<=r:
            m=(r+l)//2
            if target==nums[m]:
                first=m
                second=m
                while first>0 and nums[first-1]==target:
                    first-=1
                while second<len(nums)-1 and nums[second+1]==target:
                    second+=1
                out=[first,second] 
                return out   
            elif target>nums[m]:
                l=m+1
            else:
                r=m-1
                
        return out                        


