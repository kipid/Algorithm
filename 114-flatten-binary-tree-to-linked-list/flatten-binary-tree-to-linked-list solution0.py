# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        preRoot = TreeNode()
        def preorder(curRoot: TreeNode):
            nonlocal preRoot
            newRoot = TreeNode(curRoot.val)
            preRoot.right = newRoot
            preRoot = newRoot
            if curRoot.left:
                preorder(curRoot.left)
            if curRoot.right:
                preorder(curRoot.right)

        savePreRoot = preRoot
        preorder(root)
        root.left = None
        root.right = savePreRoot.right.right