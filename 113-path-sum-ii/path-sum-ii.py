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
        path = []
        def search(cur, sumUntil):
            path.append(cur.val)

            if not cur.left and not cur.right and sumUntil == targetSum:
                res.append(path[:]) # shallow copy of path

            if cur.left:
                search(cur.left, sumUntil+cur.left.val)
            if cur.right:
                search(cur.right, sumUntil+cur.right.val)
            path.pop()

        search(root, root.val)
        return res