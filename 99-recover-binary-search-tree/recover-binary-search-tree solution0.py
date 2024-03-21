# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder_list = []
        def inOrder(root):
            if root == None:
                return
            inOrder(root.left)
            inorder_list.append(root)
            inOrder(root.right)

        inOrder(root)

        # 4, 2, 3, 1
        misplaced = []
        for i in range(1, len(inorder_list)):
            if inorder_list[i-1].val > inorder_list[i].val:
                misplaced.append(inorder_list[i-1])
                misplaced.append(inorder_list[i])
        misplaced[0].val, misplaced[-1].val = misplaced[-1].val, misplaced[0].val