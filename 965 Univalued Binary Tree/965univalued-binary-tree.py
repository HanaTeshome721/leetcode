# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # per=None 
        # def dfs(node,per):
        #     if not node:
        #         return True
        #     if per and node.val!=per.val:
        #         return False
        #     per=node    
        #     l=dfs(node.left,per)
        #     r=dfs(node.right,per)  
        #     return l and r
        # return dfs(root,per)    

    #     q=deque([root])
    #     per=None
    #     while q:
    #         node=q.popleft()
    #         if per and per.val!=node.val:
    #             return False
    #         per=node    
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #     return True                    
                  



    #    q=deque()
    #    q.append(root)
    #    valr=root.val
    #    while q:
    #     n=q.popleft()
    #     if n.val!=valr:
    #         return False
    #     if n.left:
    #         q.append(n.left)
    #     if n.right:
    #         q.append(n.right)
    #    return True         



    #    if root.left is None and root.right is None:
    #         return True
    #     if root.left and root.left.val != root.val:
    #         return False
    #     if root.right and root.right.val != root.val:
    #         return False
    #     ret = 0
    #     if root.left:
    #         ret += self.isUnivalTree(root.left)
    #     else:
    #         ret += 1

    #     if root.right:
    #         ret += self.isUnivalTree(root.right)
    #     else:
    #         ret += 1
    #     return ret == 2



        stack = []
        curr =  root
        val = root.val

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            
            if val != curr.val:
                return False
 
            curr = curr.right
        return True
                      
