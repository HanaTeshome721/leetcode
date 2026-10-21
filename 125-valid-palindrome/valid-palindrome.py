class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        st=''
        for w in s:
            for c in w:
              if c.isalnum():
                
                st+=c.lower()
        print(st)
        l=0
        r=len(st)-1
        while l<r:
            if st[r]!=st[l]:
                return False
            l+=1
            r-=1    
        return True        