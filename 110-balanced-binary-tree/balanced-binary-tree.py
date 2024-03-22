# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def inorder(root: TreeNode, level: int, maxLevel: int) -> (int, bool):
            if not root:
                return maxLevel, True
            leftMax, leftBal = inorder(root.left, level+1, level)
            rightMax, rightBal = inorder(root.right, level+1, level)
            return max(leftMax, rightMax), leftBal and rightBal and abs(leftMax - rightMax) <= 1

        return inorder(root, 1, 1)[1]