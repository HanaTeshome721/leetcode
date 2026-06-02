class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
       n=len(edges)
       parent=[i for i in range(n+1)]
       size=[1]*(n+1)

       def find(n):
            if n!=parent[n]:
                parent[n]=find(parent[n])
            return parent[n]
       def union(x,y):
            rx,ry=find(x),find(y)
            if rx==ry:
                return False
            if size[rx]>size[ry]:
                parent[ry]=rx 
                size[rx]+=size[ry]
            else:
                parent[rx]=ry
                size[ry]+=size[rx]
            return True
       for n1,n2 in edges:
          if not union(n1,n2):
              return [n1,n2]                
