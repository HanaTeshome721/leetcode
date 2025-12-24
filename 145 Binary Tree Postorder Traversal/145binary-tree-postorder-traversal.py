# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #  ans=[]
        #  def post(node):
        #     if not node:
        #         return 
        #     post(node.left)
        #     post(node.right)
        #     ans.append(node.val) 

        #  if root:
        #     post(root)
        #  return ans           

        stack=[root]
        visited=[False]
        ans=[]
        while stack:
            cur,v=stack.pop() , visited.pop()
            if cur:
               if v:
                 ans.append(cur.val)
               else:
                    stack.append(cur)
                    visited.append(True)
                    stack.append(cur.right)
                    visited.append(False)
                    stack.append(cur.left)
                    visited.append(False)
        return ans