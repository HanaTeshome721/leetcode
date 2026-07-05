# class TrieNode:
#     def __init__(self):
#         self.children={}
#         self.end=False
# class Trie:
#     def __init__(self):
#         self.root=TrieNode()

#     def insert(self,word):
#         node=self.root
#         for c in word:
#             if c not in node.children:
#                 node.children[c]=TrieNode()
#             node=node.children[c]
#         node.end=True
#     def findp(self,word):
#         node=self.root
#         prefix=""
#         for c in word:
#             if c not in node.children:
#                 return word

#             node=node.children[c]
#             prefix+=c
#             if node.end:
#                 return prefix
#         return word                   
# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         trie=Trie()
#         for word in dictionary:
#             trie.insert(word)

#         words=sentence.split()
#         for i in range(len(words)):
#             words[i]=trie.findp(words[i])
#         return " ".join(words)       

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:


        d = []
        for i, w in enumerate(sorted(dictionary)):
            if i == 0 or (not w.startswith(d[-1])): 
                d.append(w)

        res = []
        for word in sentence.split():
            i = bisect_left(d, word)
            if i and word.startswith(d[i - 1]): res.append(d[i - 1])
            else: res.append(word)
            
        return ' '.join(res)        