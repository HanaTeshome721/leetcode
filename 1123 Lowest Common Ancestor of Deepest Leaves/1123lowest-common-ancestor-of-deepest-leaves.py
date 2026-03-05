# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

           def dfs(node,depth):
             if not node:
                return None,depth
             leftnd,ld=dfs(node.left,depth+1)    
             rightnd,rd=dfs(node.right,depth+1)   

             if ld>rd:
                return leftnd,ld
             elif rd>ld:
                return rightnd,rd
             else:
                 return node,ld
           node,_=dfs(root,0)  
           return node           


        # def dfs(root):
        #     if not root:
        #         return 0, None

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     if left[0] > right[0]:
        #         return left[0] + 1, left[1]
        #     if left[0] < right[0]:
        #         return right[0] + 1, right[1]
        #     return left[0] + 1, root

        # return dfs(root)[1]
















        