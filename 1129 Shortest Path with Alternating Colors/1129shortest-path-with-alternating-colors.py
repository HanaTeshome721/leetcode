class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
      blue=defaultdict(list)
      red=defaultdict(list)

      for i in range(len(redEdges)):
            v,u=redEdges[i]
            red[v].append(u)

        
      for i in range(len(blueEdges)):
            v,u=blueEdges[i]
            blue[v].append(u)
           

      q=deque()
      q.append([0,0,None])
      visit=set()
      visit.add((0,None))
      answer=[-1]*n

      while q:
            n,l,ec=q.popleft()
            if answer[n]==-1:
                answer[n]=l
            if ec!="RED":
                for nigh in red[n]:
                    if (nigh,"RED") not in visit:
                        visit.add((nigh,"RED"))
                        q.append([nigh,l+1,"RED"])         
            if ec!="BLUE":
                for nigh in blue[n]:
                    if (nigh,"BLUE") not in visit:
                        visit.add((nigh,"BLUE"))
                        q.append([nigh,l+1,"BLUE"])  
      return answer                            

        # graph = defaultdict(list)
        # for u, v in redEdges:
        #     graph[u].append((v, 0))
        # for u, v in blueEdges:
        #     graph[u].append((v, 1))

        # res = [-1] * n
        # q = deque([(0, -1)])
        # visited = set([(0, -1)])
        # dist = 0

        # while q:
        #     for _ in range(len(q)):
        #         node, color = q.popleft()
        #         if res[node] == -1:
        #             res[node] = dist
        #         for nei, c in graph[node]:
        #             if c != color and (nei, c) not in visited:
        #                 visited.add((nei, c))
        #                 q.append((nei, c))
        #     dist += 1
        # return res
              


       





        # graph = defaultdict(lambda: {"RED": [], "BLUE": []})

        # for u, v in redEdges:
        #     graph[u]["RED"].append(v)

        # for u, v in blueEdges:
        #     graph[u]["BLUE"].append(v)
        # queue = deque()
        # queue.append((0, None, 0))   
        # answer = [-1] * n
        # visited = set()
        # visited.add((0, None))

        # while queue:
        #     node, last_color, dist = queue.popleft()

        #     if answer[node] == -1:
        #         answer[node] = dist

            
        #     if last_color != "RED":
        #         for nei in graph[node]["RED"]:
        #             if (nei, "RED") not in visited:
        #                 visited.add((nei, "RED"))
        #                 queue.append((nei, "RED", dist + 1))

        #     if last_color != "BLUE":
        #         for nei in graph[node]["BLUE"]:
        #             if (nei, "BLUE") not in visited:
        #                 visited.add((nei, "BLUE"))
        #                 queue.append((nei, "BLUE", dist + 1))

        # return answer           