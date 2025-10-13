class Solution:
    def findWords(self, words: List[str]) -> List[str]:
    #    return list(filter(lambda word: set(word.lower())-set("qwertyuiop")==set() or
    #                               set(word.lower())-set("asdfghjkl")==set() or
    #                               set(word.lower())-set("zxcvbnm")==set(),words ))
    #    ans=[] 
    #    row=[set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]    
    #    for r in row:
    #      for word in words:
    #         lw=word.lower()
    #         if set(lw).issubset(r):
    #             ans.append(word)
    #    return ans        
       ans=[] 
       has={"r1":"qwertyuiop","r2":"asdfghjkl","r3":"zxcvbnm"}
       for word in words:
        lw=word.lower()
        for r in has.values():
            if all(ch in r for ch in lw):
                ans.append(word)
       return ans         