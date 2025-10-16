class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
    #   count=Counter(words[0])
    #   res=[]  
    #   for w in words:
    #      cur=Counter(w)
    #      for i in  count:
    #         count[i]=min(count[i],cur[i])
    #   for c in count:
    #     for i in range(count[c]):
    #         res.append(c)
    #   return res 


    
      res=[]  
      for i in set(words[0]):
        feq=min([word.count(i) for word in words])
        res+=[i]*feq  
      return res 

        # seen=[n for n in words[0]]
        # for i in range(1,len(words)):
        #     w=words[i]
        #     for c in seen[:]:
        #         if c not in w:
        #             seen.remove(c)
        #         else:
        #             w=w.replace(c,'',1)
        # return seen                