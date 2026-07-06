class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root=TrieNode()

        for word in wordDict:
            node=root
            for c in word:
                if c not in node.children:
                    node.children[c]=TrieNode()
                node=node.children[c]
            node.end=True    

        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True

        for i in range(n):
            if not dp[i]:
                continue
            node=root    
            for j in range(i,n):
                if s[j] not in node.children:
                    break
                node=node.children[s[j]]    
                if node.end:
                    dp[j+1]=True
        return dp[n]                                        
