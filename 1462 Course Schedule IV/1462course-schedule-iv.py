class Solution:
    def __init__(self):
        self.memo = {} #node, reachables

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        for p,c in prerequisites:
            graph[c].append(p)
        def dfs(cur):
            if cur not in preq:
                preq[cur]=set()
                for pr in graph[cur]:
                    preq[cur] |=dfs(pr)
                preq[cur].add(cur)
            return preq[cur]    
        preq={}        
        for n in range(numCourses):
            dfs(n)

       
        res=[]
        for u,v in queries:
            res.append(u in preq[v])
        return res    





