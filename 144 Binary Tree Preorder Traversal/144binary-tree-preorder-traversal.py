# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans=[]
        # def per(node):
        #     if not node:
        #         return
        #     ans.append(node.val)
        #     per(node.left)
        #     per(node.right)    
        # if root:
        #     per(root)
        # return  ans  


        cur=root
        stack=[]
        ans=[]
        while cur or stack:
            if cur:
                if cur.right:
                     stack.append(cur.right) 
                ans.append(cur.val)
                cur=cur.left
                
            else:
                cur=stack.pop()
        return   ans     