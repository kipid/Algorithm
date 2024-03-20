# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(begin: int, end: int) -> list[TreeNode | None]:
            if begin == end:
                return [None]

            return [
                TreeNode(root, left, right)
                for root in range(begin, end)
                for left in dfs(begin, root)
                for right in dfs(root + 1, end)
            ]
        
        return dfs(1, n + 1)