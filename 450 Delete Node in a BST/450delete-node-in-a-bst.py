# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # if not root:
        #     return None
        # if key > root.val:
        #    root.right= self.deleteNode(root.right,key)
        # elif key < root.val:
        #     root.left=self.deleteNode(root.left,key)
        # else:
        #     if not root.right:
        #         return root.left
        #     if not root.left:
        #         return root.right
        #     cur=root.right
        #     while cur.left:
        #         cur=cur.left
        #     root.val=cur.val
        #     root.right=self.deleteNode(root.right,cur.val)
        # return root                           


        if not root:
            return None
        if root.val==key:
            return self.help(root) 

        cur=root
        while cur:
            if key>cur.val:
                if cur.right and cur.right.val==key:
                    cur.right=self.help(cur.right)
                cur=cur.right 
            else:
                if cur.left and cur.left.val==key:
                    cur.left=self.help(cur.left)
                cur=cur.left 
        return root                         
    def help(self,root) :
        if not root:
            return None
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        right=root.right
        left=root.left
        while right.left:
            right=right.left
        right.left=left
        return root.right                          