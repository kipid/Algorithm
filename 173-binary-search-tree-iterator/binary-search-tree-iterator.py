# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = None
class BSTIterator:
    def inorder(self, root: Optional[TreeNode]):
        if not root:
            return
        self.inorder(root.left)
        self.prev.next = root
        self.prev = root
        root.next = None
        self.inorder(root.right)

    def __init__(self, root: Optional[TreeNode]):
        self.curr = TreeNode(-1)
        self.prev = self.curr
        self.inorder(root)

    def next(self) -> int:
        self.curr = self.curr.next
        return self.curr.val

    def hasNext(self) -> bool:
        if self.curr.next:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()