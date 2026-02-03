# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
       def valid(node,left,right):
            if not node:
                return True
            if not (node.val>left and node.val<right):
                return False 
            return valid(node.left,left,node.val) and \
                   valid(node.right,node.val,right)
       return valid(root,float("-inf"),float("inf")) 

    #    def inorder(root):
    #         if not root:
    #             return True

    #         if not inorder(root.left):
    #            return False     
    #         if root.val<=self.perv:
    #             return False
    #         self.perv=root.val
    #         return inorder(root.right)
    #    self.perv=-math.inf
    #    return inorder(root)


        # perv=None
        # def dfs(root):
        #     nonlocal perv
        #     if not root:
        #         return True
        #     if not dfs(root.left):
        #         return False    
        #     if perv is not None and root.val<=perv:
        #         return False
        #     perv=root.val    
        #     return dfs(root.right)
        # return dfs(root)    















        