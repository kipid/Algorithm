# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        kthMin = 0
        def inOrder(head):
            nonlocal n
            nonlocal kthMin
            if not head:
                return
            inOrder(head.left)
            n += 1
            if (n >= k):
                if n == k:
                    kthMin = head.val
                return
            inOrder(head.right)
        inOrder(root)
        return kthMin