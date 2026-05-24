class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pair=[(v,i) for i,v in enumerate(nums)]
        result=[0]*len(nums)

        def meres(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            left=meres(arr[:mid])    
            right=meres(arr[mid:]) 

            mere=[]
            i,j=0,0
            rightcount=0
            while i<len(left) and j<len(right):
                if left[i][0] <=right[j][0]:
                    result[left[i][1]]+=rightcount
                    mere.append(left[i])
                    i+=1
                else:
                    mere.append(right[j])
                    rightcount+=1
                    j+=1
            while i<len(left):
               
                result[left[i][1]]+=rightcount
                mere.append(left[i])
                i+=1

            while j<len(right):
                mere.append(right[j])
                j+=1
            return mere      
        meres(pair)
        return result              