# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            return l+r+1
        return dfs(root)