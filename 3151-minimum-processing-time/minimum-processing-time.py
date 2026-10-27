class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        l=len(tasks)-1
        # c=l-4
        mx=0
        for t in processorTime:
            mt=tasks[l]
            cus=t+mt
            mx=max(cus,mx)
            # c-=4
            l-=4
        return mx
            
