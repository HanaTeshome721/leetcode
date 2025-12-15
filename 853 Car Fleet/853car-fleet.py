class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #    pairs=[[p,t] for p,t in zip(position,speed)]
        #    stack=[] 
        #    for p,t in sorted(pairs)[::-1]:
        #      stack.append((target-p)/t)
        #      if len(stack)>=2 and stack[-1] <=stack[-2]:
        #         stack.pop()
        #    return len(stack)

        #    feet=[[p,t] for p,t in zip(position,speed)]
        #    feet.sort(reverse=True)

        #    stack=[]
        #    for p,t in feet:
        #       if not stack:
        #         stack.append([p,t])
        #       targett=(target-p)/t
        #       if targett<=(target-stack[-1][0])/stack[-1][1]:
        #         continue
        #       stack.append([p,t])
        #    return len(stack)       
        
        car={p:t for p,t in zip(position,speed)}
        po=sorted(car.keys(),reverse=True)
        feet=per=0
        for p in po:
            cut=(target-p)/car[p]
            if cut>per:
                feet+=1
                per=cut
        return feet        




