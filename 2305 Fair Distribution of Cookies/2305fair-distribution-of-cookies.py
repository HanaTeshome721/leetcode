class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        mn=float("inf")
        bucket=[0]*k

        def backtrack(i,bucket):
            nonlocal mn
            if i>=len(cookies):
                mn=min(mn,max(bucket))
                return mn
            if max(bucket)>mn:
                return 

            for j in range(k):
                bucket[j]+=cookies[i]
                backtrack(i+1,bucket)
                bucket[j]-=cookies[i]
        backtrack(0,bucket)
        return mn            

              

      