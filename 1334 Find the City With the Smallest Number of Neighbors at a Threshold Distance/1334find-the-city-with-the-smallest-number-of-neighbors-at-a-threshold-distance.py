class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj=defaultdict(list)
        for v1,v2,dis in edges:
            adj[v1].append((v2,dis))
            adj[v2].append((v1,dis))

        def dijkstra(src):
            heap=[(0,src)]
            visit=set()

            while heap:
                dist,node=heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei, distn in adj[node]:
                    neidist=dist + distn
                    if neidist<=distanceThreshold:
                        heapq.heappush(heap,(neidist,nei))    
            return len(visit)-1            

        res,min_count=-1,n    
        for src in range(n):
            count=dijkstra(src)
            if count<=min_count:
                res,min_count=src,count
        return res                