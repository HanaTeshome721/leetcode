class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(start,com):
            if len(com)==k:
                res.append(com.copy())
                return

            for i in range(start,n+1):
                com.append(i)
                backtrack(i+1,com)
                com.pop()
        backtrack(1,[])
        return res            