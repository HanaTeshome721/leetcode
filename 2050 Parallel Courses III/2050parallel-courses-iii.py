class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj=defaultdict(list)

        for src,dst in relations:
            adj[src].append(dst)
        maxv={}
        def dfs(k):
            if k in maxv:
                return maxv[k]
            res=time[k-1]
            for nig in adj[k]:
                res=max(res,time[k-1] +dfs(nig))
            maxv[k]=res    
            return res    

       
        for i in range(1,n+1):
            dfs(i)
        return max(maxv.values())      