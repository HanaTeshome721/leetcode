# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
       
      inord=[]
      self.inorder(root,inord)
      return self.bbst(inord,0,len(inord)-1)

    def inorder(self,root,inord):
        if not root:
            return 
        self.inorder(root.left,inord)
        inord.append(root.val)
        self.inorder(root.right,inord)
    def bbst(self,inord,s,e):
        if s>e:
            return None
        m=s+(e-s)//2
        left=self.bbst(inord,s,m-1)      
        right=self.bbst(inord,m+1,e) 

        node=TreeNode(inord[m],left,right)
        return node         