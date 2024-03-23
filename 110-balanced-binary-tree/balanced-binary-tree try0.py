# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        n = 0
        maxLevel = 1
        def inorder(root: TreeNode, level: int) -> Optional[TreeNode]:
            nonlocal n
            nonlocal maxLevel
            if not root:
                return None
            inorder(root.left, level+1)
            n += 1
            maxLevel = max(maxLevel, level)
            inorder(root.right, level+1)

        inorder(root, 1)
        print(f"{n = }, {maxLevel = }, {math.ceil(math.log2(n + 1)) = }")
        return maxLevel == math.ceil(math.log2(n + 1))