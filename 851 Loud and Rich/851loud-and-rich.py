class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # indegree=[0]*len(quiet)
        # graph=defaultdict(list)
        # for r,p in richer:
        #     graph[r].append(p)
        #     indegree[p]+=1
        # q=deque(i for i in range(len(indegree)) if indegree[i]==0)
        # answer=list(range(len(quiet)))
        # while q:
        #     r=q.popleft()
        #     for p in graph[r]:
        #         indegree[p]-=1
        #         if quiet[answer[r]]<quiet[answer[p]]:
        #             answer[p]=answer[r]
        #         if indegree[p]==0:
        #             q.append(p)   
        # return answer    


        
        graph=defaultdict(list)
        for r,p in richer:
            graph[p].append(r)
        res=[-1]*len(quiet)

        def dfs(n):
            if res[n]!=-1:
                return res[n]
            res[n]=n 
            for nig in graph[n]:
                candi=dfs(nig)
                if quiet[candi]<quiet[res[n]]:
                    res[n]=candi  
            return res[n]
        for i in range(len(quiet)):
            dfs(i)
        return res                              
