class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        graph=defaultdict(list)

        for v,u in edges:
            graph[v].append(u)  
            graph[u].append(v)  

        seen=set()
        seen.add(source)
        # stack=[source]
        # while stack:
        #     node=stack.pop()
        #     if node==destination:
        #         return True
        #     for nigh in graph[node]:
        #         if nigh not in seen:
        #             seen.add(nigh)
        #             if nigh==destination:
        #                 return True
        #             stack.append(nigh)
        # return False  

        q=deque([source])
        while q:
            node=q.popleft()
            if node==destination:
                return True
            for nigh in graph[node]:
                if nigh not in seen:
                    seen.add(nigh)
                    if nigh==destination:
                        return True
                    q.append(nigh)
        return False                    





        # def dfs(i):
        #     if i==destination:
        #         return True
        #     for neigh in graph[i]:
        #         if neigh not in seen:
        #             seen.add(neigh)
        #             if dfs(neigh):
        #                 return True
        #     return False
        # return dfs(source)  


