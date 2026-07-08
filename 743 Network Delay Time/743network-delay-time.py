class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge=defaultdict(list)

        for u,v,w in times:
            edge[u].append((w,v))
        minheap=[(0,k)]
        visit=set()
        t=0    

        while minheap:
            w1,n1=heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            t=max(w1,t)
            for w2,n2 in edge[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap,(w1+w2, n2))
        return t if len(visit)==n else -1                


    
        # graph = [[] for _ in range(n + 1)]
        # for u, v, w in times:
        #     graph[u].append((v, w))

        # dist = [float('inf')] * (n + 1)
        # dist[k] = 0

        # pq = [(0, k)]   # (distance, node)

        # while pq:
        #     du, u = heapq.heappop(pq)

        #     if du != dist[u]:
        #         continue

        #     for v, w in graph[u]:
        #         if dist[u] + w < dist[v]:
        #             dist[v] = dist[u] + w
        #             heapq.heappush(pq, (dist[v], v))

        # ans = max(dist[1:])

        # if ans == float('inf'):
        #     return -1
        # return ans   