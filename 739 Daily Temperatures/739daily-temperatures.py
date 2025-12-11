class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # ans=[0]*len(temperatures)
        # stack=[]
        # for i,t in enumerate(temperatures):
        #     while stack and stack[-1][1]<t:
        #         ind,val=stack.pop()
        #         ans[ind]=i-ind
        #     stack.append([i,t])
        # return ans        
             

        n=len(temperatures)
        s=[]
        ans=[0]*n

        for i in range(n):
            while s and temperatures[s[-1]]<temperatures[i]:
                d=s.pop()
                ans[d]=i-d
            s.append(i)
        return ans   


        # ans=[0]*len(temperatures)
        # s=[]

        # for i,t in enumerate(temperatures):
        #     while s and temperatures[s[-1]]<t:
        #         ind=s.pop()
        #         ans[ind]=i-ind
        #     s.append(i)
        # return ans    

