class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       if not s:
        return True 
       ls=len(t)
       j=0
       for i in range(ls):
            if j<len(s) and s[j]==t[i]: 
              j+=1
       return  j==len(s)         