class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
       
        cn=0
        for w in words:
            l=len(w)
            dc=Counter(chars)
            for c in w:
                if c  in chars and dc[c]>0:
                    dc[c]-=1
                    l-=1
            if not l:        
              cn+=len(w)
        return cn    
