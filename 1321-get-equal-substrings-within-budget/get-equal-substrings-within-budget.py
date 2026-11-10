class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        leng=len(s)
        ans=0
        l=0
        c=0
        for i in range(leng):
          c+=abs(ord(s[i])-ord(t[i]))
          while c>maxCost:
            c-=abs(ord(s[l])-ord(t[l]))
            l+=1
          ans=max(ans,i-l+1)              
        return ans   