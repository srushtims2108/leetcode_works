# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.maxv=0
        self.total=0
        def dfs(node,depth):
            if not node:
                return 
            if not node.left and not node.right:
                if depth>self.maxv:
                    self.maxv=depth
                    self.total=node.val
                elif depth==self.maxv:
                    self.total+=node.val
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return self.total