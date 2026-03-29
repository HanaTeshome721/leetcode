class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
       if n==1:
        return [0] 
       graph=defaultdict(list)
       for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
       egcnt={}
       q=deque()
       for src, nigh in graph.items():
            if len(nigh)==1:
                q.append(src)
            egcnt[src]=len(nigh)  
       while q:
            if n<=2:
                return list(q)
            for i in range(len(q)):
                node=q.popleft()
                n-=1
                for nig in graph[node]:
                    egcnt[nig]-=1
                    if egcnt[nig]==1:
                        q.append(nig)
