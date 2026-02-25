class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prec={i:[] for i in range(numCourses)}
        # for cur ,per in prerequisites:
        #     prec[cur].append(per)

        # def dfs(cur):
        #     if cur in visit:
        #         return False
        #     if prec[cur]==[]:
        #         return True 
        #     visit.add(cur)    
        #     for per in prec[cur]:
        #         if not dfs(per):
        #             return False
        #     visit.remove(cur)
        #     prec[cur]=[]               
        #     return True
        # visit=set()    
        # for cur in range(numCourses):
        #     if not dfs(cur):
        #         return False
        # return True  
        


        # visited = [0] * numCourses
        # courses = [[] for _ in range(numCourses)]
        # for course, prerequisite in prerequisites:
        #     courses[course].append(prerequisite)

        # def dfs(course):
        #     if visited[course] == 1:
        #         return False
            
        #     if visited[course] == 2:
        #         return True
            
        #     visited[course] = 1
        #     for prerequisite in courses[course]:
        #         if not dfs(prerequisite):
        #             return False
            
        #     visited[course] = 2
        #     return True


        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        
        # return True






        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indegree[course]+=1
            adj[pre].append(course)

        queue = deque([c for c in range(numCourses) if indegree[c] == 0])

        taken = 0
        while queue:
            cur = queue.popleft()
            taken += 1
            for nxt in adj[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return taken == numCourses              