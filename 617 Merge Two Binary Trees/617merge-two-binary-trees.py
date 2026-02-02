# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

         if not root1 and not root2:
            return None  
         if (root1 and not root2) or (root2 and not root1):
            return root1 if root1 else root2             
         mer=TreeNode(root1.val+root2.val)
         mer.left=self.mergeTrees(root1.left,root2.left)
         mer.right=self.mergeTrees(root1.right,root2.right)
         return mer


        # if not root1 and not root2:
        #     return None
        #  v1=root1.val if root1 else 0
        #  v2=root2.val if root2 else 0
        #  root=TreeNode(v1+v2)

        #  root.left=self.mergeTrees(root1.left if root1 else None , root2.left if root2 else None)
        #  root.right=self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        #  return root  


        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        # root1.val += root2.val
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)
        # return root1


        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        
        # merged = TreeNode(root1.val + root2.val)
        # merged.left = self.mergeTrees(root1.left, root2.left)
        # merged.right = self.mergeTrees(root1.right, root2.right)
        # return merged


        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        # stack=[(root1,root2)]

        # while stack:
        #     t1,t2=stack.pop()     
        #     t1.val+=t2.val
        #     if t1.right and t2.right:
        #         stack.append((t1.right,t2.right))
        #     elif not t1.right:
        #         t1.right=t2.right
        #     if t1.left and t2.left:
        #         stack.append((t1.left,t2.left))
        #     elif not t1.left:
        #         t1.left=t2.left
        # return root1                    