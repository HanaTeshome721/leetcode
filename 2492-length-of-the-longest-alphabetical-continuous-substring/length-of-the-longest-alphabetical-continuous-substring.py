class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        if len(s)==1:
            return 1
        mx=0

        for i in range(len(s)-1):
            cn=1
            while i<len(s)-1 and  ord(s[i+1])-ord(s[i])==1:
                i+=1
                cn+=1
            mx=max(cn,mx)  
        return mx      