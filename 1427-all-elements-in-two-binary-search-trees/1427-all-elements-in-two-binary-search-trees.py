# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        res=[]
        def traverse(node):
            if not node:
                return 
            res.append(node.val)
            traverse(node.right)
            traverse(node.left)
        traverse(root1)
        traverse(root2)
        res.sort()
        return res