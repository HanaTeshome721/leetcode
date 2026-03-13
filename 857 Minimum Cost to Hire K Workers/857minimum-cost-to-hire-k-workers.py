class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res=float("inf")
        pairs=[]
        for i in range(len(quality)):
            pairs.append((wage[i]/quality[i], quality[i]))
        pairs.sort(key=lambda p:p[0])  

        maxheap=[]
        total_q=0

        for rate,q in pairs:
            heapq.heappush(maxheap,-q)  
            total_q+=q

            if len(maxheap)>k:
                total_q +=heapq.heappop(maxheap)
            if len(maxheap)==k:
                res=min(
                    res,
                    total_q*rate
                )    
        return res        