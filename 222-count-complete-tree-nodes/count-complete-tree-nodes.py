# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        count = 0
        def inorderCount(root: Optional[TreeNode]):
            if not root:
                return
            inorderCount(root.left)
            nonlocal count
            count += 1
            inorderCount(root.right)
        inorderCount(root)
        return count