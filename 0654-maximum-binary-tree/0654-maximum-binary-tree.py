# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(arr):
            # base case: empty subarray
            if not arr:
                return None
            
            # step 1: find the maximum element and its index
            max_val = max(arr)
            max_idx = arr.index(max_val)
            
            # step 2: create the root node
            root = TreeNode(max_val)
            
            # step 3: recursively build left and right subtrees
            root.left = build(arr[:max_idx])
            root.right = build(arr[max_idx+1:])
            
            return root
        
        # call the recursive function
        return build(nums)
