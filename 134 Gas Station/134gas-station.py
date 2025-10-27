class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #    if sum(gas)<sum(cost):
    #     return -1
    #    total=0
    #    start=0
    #    for i in range(len(gas)):
    #      total+=gas[i]-cost[i]
    #      if total <0:
    #         total=0
    #         start=i+1
    #    return start    


    #    cg=0
    #    tg=0
    #    diff=0
    #    start=0
    #    for i in range(len(gas)):
    #     diff=gas[i]-cost[i]
    #     cg+=diff
    #     tg+=diff
    #     if cg<0:
    #         cg=0
    #         start=i+1
    #    if tg<0:
    #     return -1
    #    else:
    #     return start   





     suu=0
     s=-1
     for i in range(2*len(gas)):
        pos=i%len(gas)
        if pos==s:
            break
        suu+=gas[pos]-cost[pos]
        if suu>=0:
            if  i<len(gas) and s<0:
                s=pos 
        else:
            s=-1        
            suu=0
     return s   
        