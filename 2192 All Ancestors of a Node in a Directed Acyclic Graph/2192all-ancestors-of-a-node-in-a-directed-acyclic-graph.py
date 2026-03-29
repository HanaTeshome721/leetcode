class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)

        for f,t in edges:
            graph[t].append(f)

        def dfs(node,res):
            
            for nig in graph[node]:
                if nig not in res:
                    res.add(nig)
                    dfs(nig,res)
            return res

        ans=[]        
        for i in range(n):  
            res=dfs(i,set())
            
            ans.append(sorted(res))
        return ans         


