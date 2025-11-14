# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(node, parent=None, grandparent=None):
            if not node:
                return
            
            # If grandparent exists and is even, add node value
            if grandparent and grandparent.val % 2 == 0:
                self.total += node.val

            # Recurse deeper: shift parent → grandparent
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)

        dfs(root)
        return self.total