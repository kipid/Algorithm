# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidHelper(root: Optional[TreeNode], min_: int, max_: int) -> bool:
            if not root:
                return True
            return min_<root.val<max_ and isValidHelper(root.left, min_, root.val) and isValidHelper(root.right, root.val, max_)

        return isValidHelper(root, -math.inf, math.inf)