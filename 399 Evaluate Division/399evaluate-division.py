class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(list)
        for i ,eq in enumerate(equations):
            a,b=eq
            adj[a].append([b,values[i]])
            adj[b].append([a,1/values[i]])

        def bfs(start,target):
            if start not in adj or target not in adj:
                return -1.0
            q=deque()
            q.append([start,1])
            visit=set()
            visit.add(start)
            while q:
                n,w=q.popleft()
                if n==target:
                    return w
                for nigh, wight in adj[n]:
                    if nigh not in visit:
                        visit.add(nigh)
                        q.append([nigh,w*wight])
            return -1.0    
        return [bfs(q[0],q[1]) for q in queries]    







        adjDict = defaultdict(dict)
        answers = []

        for (varA, varB), value in zip(equations, values):
            adjDict[varA][varB] = float(value)
            adjDict[varB][varA] = float(1/value)

        for varA, varB in queries:
            if varA not in adjDict or varB not in adjDict:
                answers.append(float(-1.0))
            elif varB in adjDict[varA]:
                answers.append(adjDict[varA][varB])
            else:
                visitedVars = []
                answers.append(self.dfs(varA, varB, visitedVars, adjDict))

        return answers

    def dfs(self, varA: str, targetVarB: str, visitedVars: set[str], adjDict: dict[str, dict[str, float]]) -> float:
        if varA == targetVarB:
            # x/x = 1
            return 1.0

        visitedVars.append(varA)

        for varB in adjDict[varA]:
            if varB not in visitedVars:
                value = adjDict[varA][varB] * self.dfs(varB, targetVarB, visitedVars, adjDict)
                if value > 0:
                    return value

        return -1.0












        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val       
            graph[b][a] = 1 / val  

        
        def dfs(curr, target, visited):
            if curr == target:
                return 1.0
            visited.add(curr)
            
            for neighbor, weight in graph[curr].items():
                if neighbor in visited:
                    continue
                res = dfs(neighbor, target, visited)
                if res != -1:
                    return weight * res  
            
            return -1  

        result = []
        for a, b in queries:
            if a not in graph or b not in graph:
                result.append(-1.0)
            else:
                result.append(dfs(a, b, set()))
        return result  