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
        def search(cur, total):
            total += cur.val
            path.append(cur.val)

            if not cur.left and not cur.right and total == targetSum:
                res.append(path[:])

            if cur.left:
                search(cur.left, total)
            if cur.right:
                search(cur.right, total)
            path.pop()

        search(root, 0)
        return res