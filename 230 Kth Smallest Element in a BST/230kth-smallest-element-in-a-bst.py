# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left 
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # res=[]
        # def inor(node):
        #     if not node:
        #         return
        #     inor(node.left)
        #     res.append(node.val)
        #     inor(node.right)
        #     return res
        # inor(root)    
        # res.sort()
        # return res[k-1]    



        stack=[]
        cur=root
      
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            k-=1
            if k==0:
                return cur.val
            cur=cur.right
                 