class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
   
        graph=defaultdict(list)
        for c,per in prerequisites:
            graph[c].append(per)

        res=[]
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            
            path.add(node)    
            for nig in graph[node]:
                if not dfs(nig):
                    return False
            visit.add(node)        
            path.remove(node)
            res.append(node)
            return True


        visit=set()
        path=set()
        for  n in range(numCourses):
            if not  dfs(n):
               return []
        return res               
