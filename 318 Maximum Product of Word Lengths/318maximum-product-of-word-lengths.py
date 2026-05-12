class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # lockup=defaultdict(set)
        # for w in words:
        #     lockup[w]=set(w)
        # def check(s,j):
        #     if lockup[s] & lockup[j]:
        #         return False
        #     else:
        #        return  True        
        # maxi=0    
        # for i in words:
        #     for j in words:
        #         if check(i,j):
        #             maxi=max(maxi,len(i)*len(j))
              
        # return maxi    

        # maxi=0
        # seen=[]
        # for w in words:
        #     seen.append([set(w),len(w)])
        # print(seen)    
        # for i in range(len(seen)):
        #     for j in range(len(seen)):
        #         for c in seen[i][0]:
        #           if c in seen[j][0]:
        #             break
        #         else:
        #             maxi=max(maxi,seen[i][1]*seen[j][1])  

        # return maxi                    

      n=len(words)  
      masks=[0]*(n)

      for i ,word in enumerate(words):
            mask=0
            for c in word:
                mask |=1<<( ord(c)-ord("a"))
            masks[i]=mask
      res=0
      for i in range(n):
        for j in range(i+1,n):
            if masks[i] & masks[j]==0:
                res=max(res,len(words[i]) * len(words[j]) )          
      return res          