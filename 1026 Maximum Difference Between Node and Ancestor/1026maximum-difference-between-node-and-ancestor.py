# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
         
       def bfs(node,curmn,curmx):
            if not node:
                return curmx-curmn
            curmx=max(curmx,node.val)
            curmn=min(curmn,node.val)
            return max( bfs(node.left,curmn,curmx),bfs(node.right,curmn,curmx))
       return bfs(root,root.val,root.val)     
