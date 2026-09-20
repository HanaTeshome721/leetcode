class Solution:
    def scoreOfString(self, s: str) -> int:
        sc=0
        for i in range(1,len(s)):
            sc+=abs(ord(s[i-1])-ord(s[i]))
        return sc    