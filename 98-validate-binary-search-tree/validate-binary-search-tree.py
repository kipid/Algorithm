# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidHelper(root: Optional[TreeNode], min_: int, max_: int) -> bool:
            isValid = True
            if root.left:
                isValid = isValid and min_ < root.left.val < min(root.val, max_) and isValidHelper(root.left, min_, root.val)
            if root.right:
                isValid = isValid and max(root.val, min_) < root.right.val < max_ and isValidHelper(root.right, root.val, max_)
            return isValid

        return isValidHelper(root, -math.inf, math.inf)