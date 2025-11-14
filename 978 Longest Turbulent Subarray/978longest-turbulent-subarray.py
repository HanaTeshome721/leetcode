class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # l,r=0,1
        # pev,res='',1
        # while r<len(arr):
        #     if arr[r-1]<arr[r] and pev!='<':
        #         res=max(res,r-l+1)
        #         r+=1
        #         pev='<'
        #     elif arr[r-1]>arr[r] and pev!='>':
        #         res=max(res,r-l+1)
        #         r+=1
        #         pev='>'
        #     else:
        #         r=r+1 if arr[r-1]==arr[r] else r 
        #         l=r-1
        #         pev=''
        # return res

        flag=True
        count=1
        res=1
        for a,b in pairwise(arr):
            if a<b and flag or a>b and not flag:
                flag= not flag
                count+=1
            else:
                if count>res:
                    res=count
                count=1 if a==b else 2
        return max(res,count)            





           
      

      
        


        # ans = 1
        # up = down = 1

        # for i in range(1, len(arr)):
        #     if arr[i - 1] < arr[i]:
        #         up = down + 1
        #         down = 1
        #     elif arr[i - 1] > arr[i]:
        #         down = up + 1
        #         up = 1
        #     else:
        #         down = 1
        #         up = 1

        #     ans = max(ans, up, down)

        # return ans     
       