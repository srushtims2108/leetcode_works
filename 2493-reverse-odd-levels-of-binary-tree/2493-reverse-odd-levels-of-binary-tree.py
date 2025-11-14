# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:
        # Helper function to recursively swap mirror nodes
        def dfs(left, right, level):
            # Base condition
            if not left or not right:
                return
            
            # If current level is odd -> swap the values
            if level % 2 == 1:
                left.val, right.val = right.val, left.val
            
            # Recurse on children (mirror pairs)
            dfs(left.left, right.right, level + 1)
            dfs(left.right, right.left, level + 1)
        
        # Start recursion with root's children (level 1)
        dfs(root.left, root.right, 1)
        return root
