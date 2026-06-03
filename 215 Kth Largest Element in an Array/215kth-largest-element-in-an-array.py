import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]

        # heap=[]

        # for num in nums:
        #     heapq.heappush(heap,num)
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # return heap[0]        


        # res=heapq.nlargest(k,nums)
        # return res[k-1]


        n=len(nums)
        heap=nums[:k]
        heapq.heapify(heap)
        for i in range(k,n):
            if nums[i]>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])
        return heap[0]        
                



