class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        time=[0]*n
        t=1
        res=-1
        visit=[0]*n
        def dfs(m):
            nonlocal t ,res
            visit[m]=1
            time[m]=t
            t+=1
            nig=edges[m]
            if nig!=-1:
                if visit[nig]==0:
                    dfs(nig)
                elif visit[nig]==1:
                    res=max(res,time[m]-time[nig]+1)
            visit[m]=2        
            return res

        for i in range(n):
           if not visit[i]: 
               dfs(i)
        return res   






        # n = len(edges)
        # indegree = [0] * n

       
        # for i in range(n):
        #     if edges[i] != -1:
        #         indegree[edges[i]] += 1

        # q = deque(i for i in range(n) if indegree[i] == 0)

        # while q:
        #     node = q.popleft()
        #     nei = edges[node]

        #     if nei != -1:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)

       
        # visited = [False] * n
        # res = -1

        # for i in range(n):
        #     if indegree[i] > 0 and not visited[i]:
        #         curr = i
        #         count = 0

        #         while not visited[curr]:
        #             visited[curr] = True
        #             curr = edges[curr]
        #             count += 1

        #         res = max(res, count)

        # return res