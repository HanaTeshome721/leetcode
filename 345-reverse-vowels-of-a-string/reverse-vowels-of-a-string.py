class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        st={"a","e","i","o","u","A","E","I","O","U"}
        l=0
        r=len(s)-1
        res=''
        while l<=r:
            while s[l] not in st and l<r:
                l+=1
            while s[r] not in st and r>l:
                r-=1
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return "".join(s)       


