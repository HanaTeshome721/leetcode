class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # stack=[]
        # for c in logs:
        #     if c=="./":
        #         continue
        #     elif c=="../" and stack:
        #         stack.pop()   
        #     else:
        #        if c!="../":
        #         stack.append(c)      
        # return len(stack)  

        res=0
    
        for c in logs:
            if c=="../" and res>0:
                res-=1
            elif c!='./' and c!='../':
                res+=1
        return res            
