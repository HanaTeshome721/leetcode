class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row=len(matrix)
        col=len(matrix[0])
        heap=[]
        for r in range(row):
          for c in range(col):
            if len(heap)<k:
                heapq.heappush(heap,-matrix[r][c])
            else:
                if -heap[0]>matrix[r][c]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,-matrix[r][c])
        return -heap[0]  

        # row=len(matrix)
        # col=len(matrix[0])          
        # heap=[]

        # for r in range(row):
        #     for c in range(col):
        #         heapq.heappush(heap,matrix[r][c])

        # for i in range(k-1):
        #     heapq.heappop(heap)
        # return heap[0]            

        # n=len(matrix)
        # heap=[]
        # for r in range(n):
        #     heapq.heappush(heap,[matrix[r][0],r,0])

        # for i in range(k-1):
        #     val,r,c=heapq.heappop(heap)
        #     if c+1<n:
        #         heapq.heappush(heap,[matrix[r][c+1],r,c+1])
        # return heapq.heappop(heap)[0]        



