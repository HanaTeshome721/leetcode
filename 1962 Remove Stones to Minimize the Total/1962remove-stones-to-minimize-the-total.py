class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[]
        for p in piles:
            heapq.heappush(heap,-p)
        while k>0:
            val=heapq.heappop(heap)  
            heapq.heappush(heap,val//2)
            k-=1
        return -sum(heap)   