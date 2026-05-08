class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj=defaultdict(list)
        for i in range(len(edges)):
            src,dst=edges[i]
            adj[src].append((dst,succProb[i]))
            adj[dst].append((src,succProb[i]))
        pq=[(-1,start)]  
        visit=set()

        while pq:
            prob,cur=heapq.heappop(pq)  
            visit.add(cur)
            if cur==end:
                return prob * -1
            for nei , edgp in adj[cur]:
                if nei not in visit:
                    heapq.heappush(pq,(prob * edgp,nei))
        return 0                
