# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        values = [[root.val]]
        nodes = [[root]]

        def addLevel(preNodes: List[TreeNode]) -> bool:
            level = len(nodes)%2
            levelValues = []
            levelNodes = []
            if level:
                for node in preNodes[::-1]:
                    if node.right:
                        levelValues.append(node.right.val)
                        levelNodes.append(node.right)
                    if node.left:
                        levelValues.append(node.left.val)
                        levelNodes.append(node.left)
            else:
                for node in preNodes[::-1]:
                    if node.left:
                        levelValues.append(node.left.val)
                        levelNodes.append(node.left)
                    if node.right:
                        levelValues.append(node.right.val)
                        levelNodes.append(node.right)
            if len(levelNodes) > 0:
                values.append(levelValues)
                nodes.append(levelNodes)
                return True
            else:
                return False
        
        while addLevel(nodes[-1]):
            pass
        return values