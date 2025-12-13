class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # d={v:i for i,v in enumerate(s)}
        # st=set()
        # stack=[]

        # for i,c in enumerate(s):
        #     if c not in st:
        #         while stack and stack[-1]>c and i<d[stack[-1]]:
        #             st.discard(stack.pop())
        #         st.add(c)
        #         stack.append(c)
        # return ''.join(stack)            

        # last={v:i for i,v in enumerate(s)}
        # used=set()
        # res=''

        # for i,v in enumerate(s):
        #     if v in used:
        #         continue
        #     while res and res[-1]>v and last[res[-1]]>i:
        #         used.remove(res[-1])
        #         res=res[:-1]
        #     used.add(v)
        #     res+=v
        # return res            

        frq={}
        for c in s:
            frq[c]=frq.get(c,0) +1
        used=set()
        stack=[]

        for c in s:
            frq[c]-=1

            if c in used:
                continue
            while stack and stack[-1]>c and frq[stack[-1]]>0:
                used.remove(stack.pop())
                
            used.add(c)
            stack.append(c)
        return ''.join(stack)                