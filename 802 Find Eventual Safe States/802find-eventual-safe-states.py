class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
      n=len(graph)
    
      def dfs(node):
        if node in path:
            return False
        if node in visit:
            return True
        path.add(node)

        for nig in graph[node]:
            if not dfs(nig) :
                return False
        visit.add(node)
        path.remove(node)
        return True               

      res=[]
      path=set()
      visit=set()
      for i in range(n):
        if dfs(i):
            res.append(i)
      return res      