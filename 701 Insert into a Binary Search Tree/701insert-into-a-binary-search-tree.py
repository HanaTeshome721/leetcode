# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root:
        #     return TreeNode(val)
        # if root.val>val:
        #     root.left=self.insertIntoBST(root.left,val)
        # else:
        #     root.right=self.insertIntoBST(root.right,val)
        # return root            

        if not root:
            return TreeNode(val)
        cur=root
        while cur:
            if cur.val>val:
                if cur.left:
                    cur=cur.left  
                else:
                    cur.left=TreeNode(val)
                    return root
            elif cur.val<val:
                if cur.right:
                   cur=cur.right 
                else:
                   cur.right=TreeNode(val)
                   return root
            

        
        # if not root:
        #     return TreeNode(val)   

        # cur=root
        # while True:
        #     if cur.val<val:
        #         if not cur.right:
        #             cur.right=TreeNode(val)
        #             return root
        #         cur=cur.right
        #     else:
        #         if not cur.left:
        #             cur.left=TreeNode(val)
        #             return root
        #         cur=cur.left          

        