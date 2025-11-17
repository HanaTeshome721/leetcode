class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # num=[]
        # for i in range(len(nums)):
        #     res=1
        #     for j in range(len(nums)):
        #         if j==i:
        #             continue
        #         res*=nums[j]
        #     num.append(res)
        # print(num)

        # n=len(nums)
        # perf=1
        # ans=[1]*n
        # for i in range(n):
        #     ans[i]=perf
        #     perf*=nums[i]
        # postf=1
        # for  i in range(n-1,-1,-1):
        #     ans[i]*=postf
        #     postf*=nums[i]
        # return ans

        # n=len(nums)        
        # rnt=[1]*n
        # pos=1
        # perf=1
        # for i in range(n):
        #     rnt[i]*=pos
        #     rnt[n-i-1]*=perf
        #     pos*=nums[i]
        #     perf*=nums[n-i-1]
        # return rnt  
        n=len(nums)
        perf=[1]*n 
        postf=[1]*n
        for i in range(1,n):
            perf[i]=perf[i-1] *nums[i-1]
            postf[i]=postf[i-1]*nums[n-i]
        return [perf[i] * postf[n-i-1] for i in range(n)]     









