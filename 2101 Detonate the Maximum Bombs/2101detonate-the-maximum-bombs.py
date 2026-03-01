class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ad=defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                x1,y1,r1=bombs[i]
                x2,y2,r2=bombs[j]
                d=sqrt((x1-x2)**2 + (y1-y2)**2)
                if d<=r1:
                    ad[i].append(j) 
                if d<=r2:
                    ad[j].append(i)       

        def dfs(i,visit):
            if i in visit:
                return 0
            cn=1
            visit.add(i)    
            for j in ad[i]:
                cn+=dfs(j,visit)
            return cn
        
        mx=0
        for i in range(len(bombs)):
            mx=max(mx,dfs(i,set()))        
        return mx




















    


        # n = len(bombs)
        # adj = [[] for _ in range(n)]
        # for i in range(n):
        #     x1, y1, r1 = bombs[i]
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         x2, y2, _ = bombs[j]
        #         dx = x1 - x2
        #         dy = y1 - y2
        #         if dx*dx + dy*dy <= r1*r1:
        #             adj[i].append(j)
        # def bfs(start):
        #     visited = [False] * n
        #     q = [start]
        #     visited[start] = True
        #     skip[start] = True
        #     count = 1
        #     while q:
        #         i = q.pop()
        #         for nxt in adj[i]:
        #             if not visited[nxt]:
        #                 visited[nxt] = True
        #                 skip[nxt] = True
        #                 q.append(nxt)
        #                 count += 1
        #     return count
        # ans = 0
        # skip = [False] * n
        # for i in range(n):
        #     if skip[i]:
        #         continue
        #     size = bfs(i)
        #     if size > ans:
        #         ans = size
        # return ans           











