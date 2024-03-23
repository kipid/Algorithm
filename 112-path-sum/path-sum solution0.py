# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        res = False
        def rootToLeaf(node: TreeNode, sumUntil: int) -> bool:
            sumUntil += node.val
            nonlocal res
            if not node.left and not node.right:
                res = res or sumUntil == targetSum
            if node.left:
                res = res or rootToLeaf(node.left, sumUntil)
            if node.right:
                res = res or rootToLeaf(node.right, sumUntil)
            return res

        return rootToLeaf(root, 0)