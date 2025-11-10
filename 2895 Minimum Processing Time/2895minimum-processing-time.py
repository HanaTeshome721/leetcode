class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:      

    #      n=len(processorTime)
    #      processorTime.sort()
    #      tasks.sort(reverse=True)
    #     #  return max(p+t  for p ,t in zip(processorTime,tasks[::4])) 
    #      mx=0
    #      for i in range(n):
    #         mx=max(mx,processorTime[i]+max(tasks[i*4:i*4+4]))
    #      return mx 


    #    n=len(processorTime)
    #    processorTime.sort()
    #    tasks.sort(reverse=True)
    #    mx=0
    #    for i in range(n):
    #     mx=max(mx,processorTime[i]+task[i*4])
    #    return mx 

    #    tasks.sort(reverse=True) 
    #    processorTime.sort()
    #    n=len(processorTime)
    #    i=0
    #    res=0 
    #    for x in range(n):
    #     r=processorTime[x]+tasks[i]
    #     if r>res:
    #         res=r
    #     i+=4
    #    return res     








        # n=len(processorTime)
        # processorTime.sort()
        # tasks.sort(reverse=True)
        # # maxt=0
        # # for i in range(n):
        # #     maxt=max(maxt,processorTime[i]+max(tasks[i*4:i*4+4]))
        # # return maxt   
        # return max(p+t for p ,t in zip(processorTime,tasks[::4]) )

        res=0
        n=len(processorTime)
        processorTime.sort()
        tasks.sort(reverse=True)
        t=0
        for i in range(n):
            a=tasks[t]
            if res<processorTime[i] + a:
                res=processorTime[i] + a
            t+=4
        return res        

          