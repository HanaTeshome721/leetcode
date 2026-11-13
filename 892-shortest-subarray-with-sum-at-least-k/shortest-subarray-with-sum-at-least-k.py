class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        # res=float("inf")
        # minheap=[]
        # cursum=0
        # for r in range(len(nums)):
        #     cursum+=nums[r]
        #     if cursum>=k:
        #         res=min(res,r+1)
        #     while minheap and cursum-minheap[0][0]>=k:
        #         prefix,endinx=heapq.heappop(minheap)
        #         res=min(res,r-endinx)
        #     heapq.heappush(minheap,(cursum,r))    
        # return -1 if res==float('inf') else res    
        res=float("inf")
        q=deque()
        cursum=0
        for r in range(len(nums)):
            cursum+=nums[r]
            if cursum>=k:
                res=min(res,r+1)
            while q and cursum-q[0][0]>=k:
                prefix,endinx=q.popleft()
                res=min(res,r-endinx)
            while q and q[-1][0]>=cursum:
                q.pop()
            q.append((cursum,r))       
        return -1 if res==float('inf') else res    