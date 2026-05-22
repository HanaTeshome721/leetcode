class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(lh,rh):
            i=0
            j=0
            sortedA=[]
            while i<len(lh) and j<len(rh):
                if lh[i]<=rh[j]:
                    sortedA.append(lh[i])
                    i+=1
                else:
                    sortedA.append(rh[j])
                    j+=1
            sortedA.extend(lh[i:])
            sortedA.extend(rh[j:])
            return sortedA

        def mere(l,r,arr):
            if l==r:
                return [arr[l]]
            m=l+(r-l)//2 
            lh=mere(l,m,arr)
            rh=mere(m+1,r,arr)
            return mergesort(lh,rh)   
        return mere(0,len(nums)-1,nums)                