# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        sum_ = 0

        def rootToLeaf(root: TreeNode, val: int) -> int:
            number = val*10 + root.val
            nonlocal sum_
            if not root.left and not root.right:
                sum_ += number
                return val
            if root.left:
                rootToLeaf(root.left, number)
            if root.right:
                rootToLeaf(root.right, number)
        
        rootToLeaf(root, 0)
        return sum_