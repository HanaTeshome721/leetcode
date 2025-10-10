class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
    #    res=0
    #    count=Counter(chars)

    #    for w in words:
    #       curt=Counter(w)
    #       good=True
    #       for c in w:
    #          if c not in count  or  curt[c]>count[c]:
    #             good=False
    #             break
    #       if good:    
    #          res+=len(w)
    #    return res      
			 
        ch = {}
        for c in chars:
            ch[c] = 1+ch.get(c, 0)
        res = 0
        
        for word in words:
            cp_ch = ch.copy()
            for l in word:
                if l in cp_ch and cp_ch[l] != 0:
                    cp_ch[l] -= 1
                else:
                    res -= len(word)
                    break
            res += len(word)
        return res
				
			
			