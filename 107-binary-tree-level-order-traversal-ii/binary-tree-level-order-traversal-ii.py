# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        values = [[root.val]]
        nodes = [[root]]

        def addLevel(levelNodes: List[TreeNode]) -> bool:
            nextValues = []
            nextNodes = []
            for levelNode in levelNodes:
                if levelNode.left:
                    nextValues.append(levelNode.left.val)
                    nextNodes.append(levelNode.left)
                if levelNode.right:
                    nextValues.append(levelNode.right.val)
                    nextNodes.append(levelNode.right)
            if len(nextNodes) > 0:
                values.append(nextValues)
                nodes.append(nextNodes)
                return True
            else:
                return False
        
        while addLevel(nodes[-1]):
            pass
        return values[::-1]