class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited=set()
        # q=deque([0])
        # visited.add(0)
        # while q:
        #     n=q.popleft()
        #     for k in rooms[n]:
        #         if k not in visited:
        #             visited.add(k)
        #             q.append(k)
        # return len(visited)==len(rooms)   


        def dfs(n):
            if not rooms[n]:
                return
            for k in rooms[n]:
                if k not in v:
                    v.add(k) 
                    dfs(k)   
        v=set()
        v.add(0)            
        dfs(0) 
        return len(v)==len(rooms)           