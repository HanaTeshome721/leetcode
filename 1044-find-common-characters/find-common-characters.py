class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        ans=[]
        if len(words)<2:
            for c in words[0]:
                ans.append(c)
            return ans    
        indx=defaultdict(defaultdict)
        for i,w in enumerate(words):
            indx[i]=Counter(w)
           
        
        for i in range(len(words[0])):
          
            for j in range(1,len(words)):
                if words[0][i] in words[j] and indx[j][words[0][i]]>0:
                       indx[j][words[0][i]]-=1
                       if j==len(words)-1:
                            ans.append(words[0][i])   
                else:
                    break                
                

        return ans      