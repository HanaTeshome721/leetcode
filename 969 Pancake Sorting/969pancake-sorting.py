class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
      
        # ans=[]
        # n=len(arr)
        # for maxn in range(n,1,-1):
        #     ind=arr.index(maxn)
        #     arr[:ind+1]=reversed(arr[:ind+1])
        #     ans.append(ind+1)
        #     arr[:maxn]=reversed(arr[:maxn])
        #     ans.append(maxn)
        # return ans    
        
        # res=[]
        # for lastindx in range(len(arr),1,-1):
        #     curindx=arr.index(lastindx)
        #     res.extend([curindx +1,lastindx])
        #     arr=arr[:curindx:-1] + arr[:curindx]
        # return res   
         
        # if not arr:
        #     return []
        # res=[]
        # for i in range(len(arr),1,-1):
        #     maxi=arr.index(i)

        #     if maxi==(len(arr)):
        #         continue
        #     if maxi!=0:
        #         res.append(maxi+1)
        #         arr[:maxi+1]=arr[:maxi+1][::-1]
        #     res.append(i)
        #     arr[:i]=arr[:i][::-1]
        # return res   

        def flip(end):
            start=0
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1


        n=len(arr)        
        output=[]
        for i in range(n-1,-1,-1):
            maxi=i
            for j in range(i,-1,-1):
                if arr[j]>arr[maxi]:
                    maxi=j
            if maxi!=i:
                flip(maxi)
                flip(i)
                output.append(maxi+1)
                output.append(i+1)
        return output                                     

