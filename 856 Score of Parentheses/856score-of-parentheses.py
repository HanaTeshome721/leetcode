class Solution:
    def scoreOfParentheses(self, s: str) -> int:
            # stack=[]
            # score=0

            # for c in s:
            #     if c=="(":
            #         stack.append(score)
            #         score=0
            #     else:
            #         score=stack.pop() + (1 if not score else 2*score)
            #         # score+= stack.pop() + max(1,score) 
            # return score                       

            # stack=[0]

            # for c in s:
            #     if c=="(":
            #         stack.append(0)
            #     else:
            #         v=stack.pop()
            #         stack[-1]+=max(1,2*v) 
            # return stack[0]           

            stack=[]
            count=0
            score=0

            for i in range(len(s)):
                if s[i]=="(":
                    stack.append(s[i])
                    count+=1
                else:
                    count-=1
                    stack.pop()
                    if s[i-1]=="(":
                        score+=2**count
            return score            















