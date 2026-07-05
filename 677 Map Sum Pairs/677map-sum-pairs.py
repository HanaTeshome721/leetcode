class Trie:
    def __init__(self):
        self.children={}
        self.sum=0

class MapSum:

    def __init__(self):
        self.root=Trie()
        self.origin={}
        

    def insert(self, key: str, val: int) -> None:
        node=self.root
        diff=val-self.origin.get(key,0)
        self.origin[key]=val

        for c in key:
            if c not in node.children:
                node.children[c]=Trie()
            node=node.children[c]
            node.sum+=diff        

    def sum(self, prefix: str) -> int:
        node=self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node=node.children[c]
        return node.sum        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)