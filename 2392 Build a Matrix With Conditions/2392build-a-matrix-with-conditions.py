class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src,adj,visit,path,order):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for nig in adj[src]:
                if not dfs(nig,adj,visit,path,order):
                    return False
            path.remove(src)
            order.append(src)
            return True        


        def topd(edges):
            adj=defaultdict(list)
            for src,dst in edges:
                adj[src].append(dst)

            visit,path=set(),set()
            order=[]

            for src in range(1,k+1):
                if not dfs(src,adj,visit,path,order):
                    return []
            return order[::-1]            

        row=topd(rowConditions)
        col=topd(colConditions)

        if not row or not col:
            return []
        valr={n:i for i,n in enumerate(row)}    
        valc={n:i for i,n in enumerate(col)} 
        res=[[0]*k for _ in range(k)]

        for num in range(1,k+1):
            r,c=valr[num],valc[num]
            res[r][c]=num
        return res       