class Solution:
    def splitString(self, s: str) -> bool:
        # def dfs(index,perv):
        #     if index==len(s):
        #         return True
        #     for j in range(index,len(s)):
        #         val=int(s[index:j+1])
        #         if val +1==perv and dfs(j+1,val):
        #             return True
        #     return False           

        # for i in range(len(s)-1):
        #     val=int(s[:i+1])
        #     if dfs(i+1,val):
        #         return True
        # return False


        # cur=[]
        # def backtrack(indx):
        #     if indx>=len(s):
        #         for i in range(1,len(cur)):
        #             if cur[i-1]-cur[i]!=1:
        #                 return False
        #         return len(cur)>=2        

        #     for i in range(indx,len(s)):
        #          val=int(s[indx:i+1])
        #          if len(cur)==0 or val+1==cur[-1]:
        #             cur.append(val) 
        #             if backtrack(i+1):
        #                 return True
        #             cur.pop()
        #     return False                       
        # return backtrack(0)

        def bck(ind):
            if ind==len(s):
                return len(cur)>=2
            for i in range(ind,len(s)):
                v=int(s[ind:i+1])
                if not cur or cur[-1]==v+1:
                    cur.append(v)
                    if bck(i+1):
                        return True
                    cur.pop()
            return False            

        cur=[]
        return bck(0)    

        








