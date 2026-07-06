# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         res=[]
#         products.sort()
#         l,r=0,len(products)-1
#         for i in range(len(searchWord)):
#             c=searchWord[i]
#             while l<=r and (len(products[l])<=i or products[l][i]!=c):
#                 l+=1
#             while l<=r and (len(products[r]) <=i or products[r][i] !=c):
#                 r-=1    
#             res.append([]) 
#             remain=r-l+1
#             for j in range(min(3,remain)):
#                 res[-1].append(products[l+j])
#         return res 



class TrieNode:
    def __init__(self):
        self.children={}
        self.suggest=[]
class Trie:
    def __init__(self):
        self.root=TrieNode()        
    def insert(self,word):
        node=self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node=node.children[c]
            if len(node.suggest)<3:
                node.suggest.append(word)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
           
        trie=Trie()
        products.sort()          
        for word in products:
            trie.insert(word)
        res=[]
        node=trie.root    
        for  c in searchWord:
            if node and c in node.children:
                node=node.children[c]
                res.append(node.suggest)
                
            else:
                node=None
                res.append([])
        return res        

