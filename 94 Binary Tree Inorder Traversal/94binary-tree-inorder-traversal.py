# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans=[]
        # def inor(node):
        #     if not node:
        #         return
        #     inor(node.left)
        #     ans.append(node.val)
        #     inor(node.right)    
        # if root:
        #     inor(root)
        # return ans    

    #    stack=[]
    #    ans=[]
    #    cur=root
    #    while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             cur=cur.left
    #         node=stack.pop()
    #         ans.append(node.val)
    #         cur=node.right
    #    return ans 

        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)    