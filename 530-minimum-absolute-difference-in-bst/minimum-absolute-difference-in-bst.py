# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDiff = math.inf
        preVal = -math.inf
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            nonlocal minDiff
            nonlocal preVal
            if (root.val - preVal) < minDiff:
                minDiff = root.val - preVal
            preVal = root.val
            inOrder(root.right)
        inOrder(root)
        return minDiff