class Union:
    def __init__(self):
        self.parent=list(range(26))
    def find(self,n1):
        if n1!=self.parent[n1]:
            self.parent[n1]=self.find(self.parent[n1])
        return self.parent[n1]
    def union(self,n1,n2):
        self.parent[self.find(n1)]=self.find(n2)     
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        un=Union()
        for e in equations:
            if e[1]=="=":
                x=ord(e[0])- ord("a")
                y=ord(e[3])-ord("a")
                un.union(x,y)
        for e in equations:
            if e[1]=="!":
                x=ord(e[0])-ord("a")        
                y=ord(e[3])-ord("a")  
                if un.find(x)==un.find(y):
                    return False
        return True             


        