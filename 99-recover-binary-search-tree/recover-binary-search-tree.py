# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorderBST(root):
            if root:
                inorderBST(root.left)
                if self.prev.val > root.val:
                    if not self.first:
                        self.first = self.prev
                    self.second = root
                self.prev = root
                inorderBST(root.right)

        self.prev = TreeNode(-math.inf)
        self.first = self.second = None
        inorderBST(root)
        self.first.val, self.second.val = self.second.val, self.first.val