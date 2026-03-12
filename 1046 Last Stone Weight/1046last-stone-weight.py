class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for st in stones:
          heapq.heappush(heap,-st)
        while len(heap)>1:  
            
            if heap[0]==heap[1]:
                heapq.heappop(heap)
                heapq.heappop(heap)
                
            else:
                x=-1*heapq.heappop(heap)
                y=-1*heapq.heappop(heap) 
                heapq.heappush(heap,y-x)
        return -1*heap[0] if heap else 0    

                