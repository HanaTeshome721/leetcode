# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
           if k==0:
            return [target.val] 
           graph=defaultdict(list)
           q=deque()
           q.append(root)
           while q:
             n=q.popleft()
             if n.left:
                graph[n].append(n.left)
                graph[n.left].append(n)
                q.append(n.left)
             if n.right:
                graph[n].append(n.right)
                graph[n.right].append(n)
                q.append(n.right)
           res=[]
           q=deque()
           q.append((target,0))
           visit=set()
           visit.add(target)
           while q:
            n,dis=q.popleft()
            if k==dis:
                res.append(n.val)
            for nig in graph[n]:
                if nig not in visit:
                    visit.add(nig)
                    q.append((nig,dis+1))
           return res         













        # if k==0:
        # # if k == 0:
        #     return [target.val]
            
        # # Phase 1: Build undirected graph using DFS
        # graph = defaultdict(list)
        
        # def build_graph(node, parent):
        #     if not node:
        #         return
        #     if parent:
        #         graph[node].append(parent)
        #         graph[parent].append(node)
        #     build_graph(node.left, node)
        #     build_graph(node.right, node)
        
        # build_graph(root, None)
        
        # # Phase 2: DFS from target to find nodes at distance k
        # res = []
        # visited = set()
        
        # def dfs(node, distance):
        #     if not node or node in visited:
        #         return
        #     visited.add(node)
            
        #     if distance == k:
        #         res.append(node.val)
        #         return
            
        #     for neighbor in graph[node]:
        #         dfs(neighbor, distance + 1)
        
        # dfs(target, 0)
        # return res






        # parent = {}
        # queue = deque()
        # queue.append(node)
        # while queue:
        #     node = queue.popleft()
        #     if node.left:
        #         parent[node.left] = node
        #         queue.append(node.left)
        #     if node.right:
        #         parent[node.right] = node
        #         queue.append(node.right)
        # visited = set()
        # visited.add(target)
        # queue.append(target)
        # dist = 0
        # while queue:
        #     if dist == k:
        #         return [node.val for node in queue]
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         for nei in (node.left,node.right,parent.get(node)):
        #             if nei and nei not in visited:
        #                 visited.add(nei)
        #                 queue.append(nei)
        #     dist+=1
        # return []

        