class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for o in operations:
            if o not in ('+','D','C'):
                stack.append(int(o))
            elif o=="+":
                n=stack[-1] + stack[-2]
                stack.append(n)
            elif o=="D":
                n=2 * stack[-1]
                stack.append(n)
            elif o=="C":
                stack.pop()
            
        return sum(stack)                    