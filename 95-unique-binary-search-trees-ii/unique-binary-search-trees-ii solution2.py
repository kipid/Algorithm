# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def buildTree(begin: int, end: int) -> list[TreeNode | None]:
            if begin == end:
                return [None]

            return [
                TreeNode(root, left, right)
                for root in range(begin, end)
                    for left in buildTree(begin, root)
                        for right in buildTree(root + 1, end)
            ]
        
        return buildTree(1, n + 1)