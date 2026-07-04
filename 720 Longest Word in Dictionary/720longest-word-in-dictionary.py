class Trie:
    def __init__(self):
        self.children={}
        self.end=False
class Solution:
    def longestWord(self, words):
        trie=Trie()
        for w in words:
            node=trie
            for c in w:
                if c not in node.children:
                    node.children[c]=Trie()
                node=node.children[c] 
            node.end=True
        self.ans=""
        def dfs(node,path):
            if node !=trie and not node.end:
                return 
            if len(path)> len(self.ans) or \
              ( len(path)==len(self.ans) and path<self.ans):
                self.ans=path
            for c in sorted(node.children.keys()):
                dfs(node.children[c], path+c)
        dfs(trie,'') 
        return self.ans     





# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         words.sort()
#         words_set, res = set(['']), ""
#         for word in words:
#             if word[:-1] in words_set:
#                 words_set.add(word)
#                 if len(word) > len(res):
#                     res = word
#         return res      

       

