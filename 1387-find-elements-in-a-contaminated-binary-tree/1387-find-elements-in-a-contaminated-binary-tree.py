# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.val=set()
        def dfs(rootnode,val):
                if not rootnode:
                    return
                rootnode.val=val
                self.val.add(rootnode.val)
                dfs(rootnode.right,2*rootnode.val+2)
                dfs(rootnode.left,2*rootnode.val+1)
        dfs(root, 0)
           

    def find(self, target: int) -> bool:
        return target in self.val


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)