# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 1
        nodes = [[root]]

        def nextLevel(preNodes: List[TreeNode]) -> bool:
            levelNodes = []
            for preNode in preNodes:
                if preNode.left:
                    levelNodes.append(preNode.left)
                if preNode.right:
                    levelNodes.append(preNode.right)
            if len(levelNodes) > 0:
                nodes.append(levelNodes)
                return True
            return False
        
        while nextLevel(nodes[-1]):
            res += 1
        return res