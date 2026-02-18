class Solution:
    def majorityElement(self, nums: List[int]) -> int:
              # nums.sort()
        # return nums[len(nums)//2]

        # hash=defaultdict(int)
        # for i in nums:
        #     if i in hash:
        #         hash[i]+=1
        #     else:
        #          hash[i]=1
          
        # for v,i in hash.items():
        #     if i >len(nums)//2:
        #         return v   
        # lead=0
        # for i in nums:
        #     if lead==0:
        #         current=i
        #     lead+=1 if current ==i else -1
        # return current  

        # count={}
        # res,maxcount=0,0
        # for n in nums:
        #     count[n] = 1+ count.get(n,0)
        #     res= n if count[n]>maxcount else res
        #     maxcount=max(maxcount,count[n])
        # return res    
        


        def maj(lo,hi):
            if lo==hi:
                return nums[lo]
            m=(lo+hi)//2    
            left=maj(lo,m)    
            right=maj(m+1,hi)

            if left==right:
                return left 
            lm=sum(1 for i in range(lo,hi+1) if nums[i]==left)       
            rm=sum(1 for i in range(lo,hi+1) if nums[i]==right) 
            return left if lm>rm else right
        return maj(0,len(nums)-1)          