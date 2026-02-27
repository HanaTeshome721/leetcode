# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        # def dfs(node,p=None,gp=None):
        #     if not node:
        #       return 0
        #     total=0
        #     if gp and gp.val%2==0:
        #         total=node.val
        #     total+=dfs(node.left,node,p)    
        #     total+=dfs(node.right,node,p) 
        #     return total
        # return dfs(root)       

        def dfs(node,p,gp):
            if not node: 
                return 0
            total=0
            if gp:
                total+=node.val
            return total + dfs(node.left,node.val%2==0,p) + dfs(node.right,node.val%2==0,p)
        return dfs(root,False,False)    

        # ans=0
        # q=deque()
        # q.append((root,None,None))
        # while q: 
        #     node,p,gp=q.popleft()
        #     if gp and gp.val%2==0:
        #         ans+=node.val   
        #     if node.left:
        #         q.append((node.left,node,p))
        #     if node.right:
        #         q.append((node.right,node,p))
        # return ans            








