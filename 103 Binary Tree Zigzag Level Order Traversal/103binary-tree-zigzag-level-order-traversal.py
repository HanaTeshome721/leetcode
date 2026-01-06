# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #   res=[]
    #   q=deque([root] if root else [])
    #   while q:
    #         level=[]
    #         for i in range(len(q)):
    #             node=q.popleft()
    #             level.append(node.val)
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
                
    #         level=list(reversed(level)) if len(res)%2 else level
    #         res.append(level)
    #   return res  

    #   res=[]
    #   q=deque([root] if root else [])
    #   zigzag=False
    #   while q:
    #     level=[]
    #     for i in range(len(q)):
    #         node=q.popleft()
    #         if node:
    #             level.append(node.val)
    #             q.append(node.left)
    #             q.append(node.right)
    #     if level:
    #         if zigzag:
    #             level.reverse()
    #             res.append(level)
    #             zigzag=False
    #         else:
    #             res.append(level)
    #             zigzag=True 
    #   return res                  

        ans=defaultdict(list)
        def dfs(node,level):
            if not node:
                return
            ans[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0) 
        res=[]
        for i in range(len(ans)):        
            if i%2:
                res.append(ans[i][::-1])
            else:
                res.append(ans[i])
        return res            