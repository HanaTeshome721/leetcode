# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
    #    per=strs[0]
    #    leper=len(per)

    #    for s  in strs[1:]:
    #       while per!=s[:leper]:
    #          leper-=1
    #          per=per[:leper]
    #    return per
    #    strs.sort() 
    #    fri=strs[0]
    #    last=strs[-1]
    #    res=''
    #    for i in range(min(len(fri),len(last))):
         
    #      if fri[i]==last[i]:
    #         res+=fri[i]
            
    #      else: break  
    #    return res   
        #  res=''
        #  for i in range(len(strs[0])): 
        #     for ch in strs:
        #         if  i>=len(ch) or ch[i]!=strs[0][i]:
        #             return res
        #     res+=ch[i]  
        #  return res          

class Trie:
    def __init__(self):
        self.children={}
        self.end=False
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie=Trie()
        
        for word in strs:
            cur=trie
            for c in word:
                if c not in cur.children:
                    cur.children[c]=Trie()
                cur=cur.children[c]
            cur.end=True
        pre=""
        cur=trie
        while True:
            if len(cur.children)!=1 or cur.end:
                break
            c=list(cur.children.keys())[0]
            pre+=c
            cur=cur.children[c]
        return pre                