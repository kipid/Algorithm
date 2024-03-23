# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def rootToLeaf(node: TreeNode, sumUntil: int, path: List[int]):
            sumUntil += node.val
            path = path + [node.val]
            if not node.left and not node.right:
                if sumUntil == targetSum:
                    res.append(path)
            if node.left:
                rootToLeaf(node.left, sumUntil, path)
            if node.right:
                rootToLeaf(node.right, sumUntil, path)
        
        rootToLeaf(root, 0, [])
        return res