# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        nodes = [[root]]
        minDepth = 1
        def helper(preNodes: TreeNode) -> bool:
            nextNodes = []
            for preNode in preNodes:
                if not preNode.left and not preNode.right:
                    return False
                if preNode.left:
                    nextNodes.append(preNode.left)
                if preNode.right:
                    nextNodes.append(preNode.right)
            nodes.append(nextNodes)
            nonlocal minDepth
            minDepth += 1
            return True
        
        while helper(nodes[-1]):
            pass
        return minDepth