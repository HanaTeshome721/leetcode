class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        de={ "{":"}","(":")" , "[":"]"}

        for c in s:
           if c in de:
              stack.append(de[c])
           else:
              if not stack or stack.pop()!=c:
                return False   

        return len(stack)==0    

        #  stack=[]
        #  de={"}":"{","]":"[",")":"("}   

        #  for c in s:
        #     if c in de:
        #         if stack and stack[-1]== de[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        #  return True if len(stack)==0 else False                                     