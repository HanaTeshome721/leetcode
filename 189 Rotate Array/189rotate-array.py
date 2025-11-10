class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k=k%len(nums)
        # l=0
        # r=len(nums)-1
        # while l<r:
        #     nums[r],nums[l]=nums[l],nums[r]
        #     r-=1
        #     l+=1
        # l,r=0 ,k-1
        # while l<r:
        #     nums[r],nums[l]=nums[l],nums[r]
        #     r-=1
        #     l+=1
        # l,r=k,len(nums)-1
        # while l<r:
        #     nums[r],nums[l]=nums[l],nums[r]
        #     l+=1
        #     r-=1        
 

        # k=k%len(nums)
        # nums[:]=nums[-k:] + nums[:-k]


        # n=len(nums)
        # k%=n
        # nums[:n-k]=reversed(nums[:n-k])
        # nums[n-k:]=reversed(nums[n-k:])
        # nums.reverse()

        n=len(nums)
        k%=n
        nums.reverse()
        # nums[:]=nums[::-1]
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]
























